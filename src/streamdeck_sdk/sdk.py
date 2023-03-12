import argparse
import json
import logging
from pathlib import Path
from typing import Optional, Callable, List

import pydantic
import websocket

from . import registration_objs
from .event_routings import EventRoutingObj, ACTION_EVENT_ROUTING_MAP, EVENT_ROUTING_MAP
from .logger import logger, init_logger, log_errors
from .mixins import SendMixin, APIEventHandlersMixin, ActionEventHandlersMixin, EventsSentMixin


class Action(
    ActionEventHandlersMixin,
    EventsSentMixin,
    SendMixin,
):
    UUID: str  # Required

    def __init__(self):
        self.plugin_uuid: Optional[str] = None
        self.ws: Optional[websocket.WebSocketApp] = None


class StreamDeck(
    ActionEventHandlersMixin,
    APIEventHandlersMixin,
    EventsSentMixin,
    SendMixin,
):
    def __init__(
            self,
            actions: List[Action] = None,
            *,
            log_file: Path = None,
            log_level: int = logging.DEBUG,
    ):
        if log_file is not None:
            self.log_file: Path = Path(log_file)
        else:
            self.log_file = None
        self.log_level = log_level
        if self.log_file is not None:
            init_logger(log_file=self.log_file, log_level=self.log_level)

        self.actions_list = actions
        self.actions = {}

        self.ws: Optional[websocket.WebSocketApp] = None
        self.port: Optional[int] = None
        self.plugin_uuid: Optional[str] = None
        self.register_event: Optional[str] = None
        self.info: [registration_objs.Info] = None

        self.registration_dict: Optional[dict] = None

    @log_errors
    def ws_on_open(
            self,
            ws: websocket.WebSocketApp,  # noqa
    ) -> None:
        logger.info("WS OPENED")
        self.send(data=self.registration_dict)

    @log_errors
    def ws_on_close(
            self,
            ws: websocket.WebSocketApp,  # noqa
            close_status_code: int,
            close_msg: str,
    ) -> None:
        logger.debug(f"{close_status_code=}; {close_msg=}")
        logger.info(f"WS CLOSED")

    @log_errors
    def ws_on_message(
            self,
            ws: websocket.WebSocketApp,  # noqa
            message: str,
    ) -> None:
        message_dict = json.loads(message)
        logger.debug(f"{message_dict=}")

        event = message_dict["event"]
        logger.debug(f"{event=}")

        event_routing = EVENT_ROUTING_MAP.get(event)
        if event_routing is None:
            logger.warning("event_routing is None")
            return

        obj = event_routing.obj.parse_obj(message_dict)
        logger.debug(f"{obj=}")

        self.route_event_in_sd_handler(event_routing=event_routing, obj=obj)
        if event in ACTION_EVENT_ROUTING_MAP:
            self.route_event_in_action_handler(event_routing=event_routing, obj=obj)

    @log_errors
    def ws_on_error(
            self,
            ws: websocket.WebSocketApp,  # noqa
            error: str,
    ) -> None:
        logger.error(f"{error=}")

    @log_errors
    def route_event_in_sd_handler(
            self,
            event_routing: EventRoutingObj,
            obj: pydantic.BaseModel
    ) -> None:
        handler: Callable = getattr(self, event_routing.handler_name)
        if handler is None:
            message = "Handler is None"
            logger.error(message)
            raise ValueError(message)
        handler(obj=obj)

    @log_errors
    def route_event_in_action_handler(
            self,
            event_routing: EventRoutingObj,
            obj: pydantic.BaseModel,
    ) -> None:
        try:
            action_uuid = getattr(obj, "action")
        except AttributeError as err:
            logger.warning(str(err), exc_info=True)
            return
        action_obj = self.actions.get(action_uuid)
        if action_obj is None:
            logger.info(f"{action_uuid=} not registered")
            return

        handler: Callable = getattr(action_obj, event_routing.handler_name)
        if handler is None:
            message = "Handler is None"
            logger.error(message)
            raise ValueError(message)
        handler(obj=obj)

    @log_errors
    def run(self) -> None:
        logger.debug(f"Plugin has been launched")
        parser = argparse.ArgumentParser(description='StreamDeck Plugin')
        parser.add_argument('-port', dest='port', type=int, help="Port", required=True)
        parser.add_argument('-pluginUUID', dest='pluginUUID', type=str, help="pluginUUID", required=True)
        parser.add_argument('-registerEvent', dest='registerEvent', type=str, help="registerEvent", required=True)
        parser.add_argument('-info', dest='info', type=str, help="info", required=True)

        args = parser.parse_args()
        logger.debug(f"{args=}")

        self.port: int = args.port
        logger.debug(f"{self.port=}")
        self.plugin_uuid: str = args.pluginUUID
        logger.debug(f"{self.plugin_uuid=}")
        self.register_event: str = args.registerEvent
        logger.debug(f"{self.register_event=}")
        self.info: registration_objs.Info = registration_objs.Info.parse_obj(json.loads(args.info))
        logger.debug(f"{self.info=}")

        self.registration_dict = {"event": self.register_event, "uuid": self.plugin_uuid}
        logger.debug(f"{self.registration_dict=}")
        self.ws = websocket.WebSocketApp(
            'ws://localhost:' + str(self.port),
            on_message=self.ws_on_message,
            on_error=self.ws_on_error,
            on_close=self.ws_on_close,
            on_open=self.ws_on_open,
        )
        self.__init_actions()
        self.ws.run_forever()

    def __init_actions(self) -> None:
        if self.actions_list is None:
            return

        for action in self.actions_list:
            try:
                action_uuid = action.UUID
            except AttributeError:
                action_class = str(action.__class__)
                message = f"{action_class} must have attribute UUID"
                logger.error(message)
                raise AttributeError(message)
            action.ws = self.ws
            action.plugin_uuid = self.plugin_uuid
            self.actions[action_uuid] = action
