import json
import logging
from typing import Callable

import pydantic

from . import event_routings
from .logger import (
    log_errors,
)
from .mixins import EventsSendMixin
from .simple_ws.client import WebSocketClientApp

logger = logging.getLogger(__name__)


class EventRoutingMixin(EventsSendMixin):
    registration_dict: dict
    actions: dict

    @log_errors
    def ws_on_open(
            self,
            ws: WebSocketClientApp,  # noqa
    ) -> None:
        logger.info("WS OPENED")
        self.send(data=self.registration_dict)

    @log_errors
    def ws_on_close(
            self,
            ws: WebSocketClientApp,  # noqa
            close_status_code: int,
            close_msg: str,
    ) -> None:
        logger.debug(f"{close_status_code=}; {close_msg=}")
        logger.info(f"WS CLOSED")

    @log_errors
    def ws_on_error(
            self,
            ws: WebSocketClientApp,  # noqa
            error,
    ) -> None:
        logger.error(f"{error=}")

    @log_errors
    def ws_on_message(
            self,
            ws: WebSocketClientApp,  # noqa
            message: str,
    ) -> None:
        logger.info(f"Message processing has started. message={message}")
        message_dict = json.loads(message)
        logger.debug(f"{message_dict=}")
        event = message_dict["event"]
        logger.debug(f"{event=}")
        event_routing = event_routings.EVENT_ROUTING_MAP.get(event)
        if event_routing is None:
            logger.warning("event_routing is None")
            return

        obj = event_routing.obj_type.model_validate(message_dict)
        logger.debug(f"{obj=}")

        self.route_event_in_plugin_handler(event_routing=event_routing, obj=obj)
        if event_routing.type is event_routings.EventRoutingObjTypes.ACTION:
            self.route_action_event_in_action_handler(event_routing=event_routing, obj=obj)
        elif event_routing.type is event_routings.EventRoutingObjTypes.PLUGIN:
            self.route_plugin_event_in_action_handlers(event_routing=event_routing, obj=obj)
        logger.info(f"Message processing completed. message={message}")

    @log_errors
    def route_event_in_plugin_handler(
            self,
            event_routing: event_routings.EventRoutingObj,
            obj: pydantic.BaseModel,
    ) -> None:
        try:
            handler: Callable = getattr(self, event_routing.handler_name)
        except AttributeError as err:
            logger.error(f"Handler missing: {str(err)}", exc_info=True)
            return
        self.handle_message(handler=handler, obj=obj)

    @log_errors
    def route_action_event_in_action_handler(
            self,
            event_routing: event_routings.EventRoutingObj,
            obj: pydantic.BaseModel,
    ) -> None:
        try:
            action_uuid = getattr(obj, "action")
        except AttributeError as err:
            logger.error(str(err), exc_info=True)
            return
        action_obj = self.actions.get(action_uuid)
        if action_obj is None:
            logger.warning(f"{action_uuid=} not registered")
            return
        try:
            handler: Callable = getattr(action_obj, event_routing.handler_name)
        except AttributeError as err:
            logger.error(f"Handler missing: {str(err)}", exc_info=True)
            return
        self.handle_message(handler=handler, obj=obj)

    @log_errors
    def route_plugin_event_in_action_handlers(
            self,
            event_routing: event_routings.EventRoutingObj,
            obj: pydantic.BaseModel,
    ) -> None:
        for action_obj in self.actions.values():
            try:
                handler: Callable = getattr(action_obj, event_routing.handler_name)
            except AttributeError as err:
                logger.error(f"Handler missing: {str(err)}", exc_info=True)
                return
            self.handle_message(handler=handler, obj=obj)

    @log_errors
    def handle_message(
            self,
            handler: Callable,
            obj: pydantic.BaseModel
    ) -> None:
        try:
            handler(obj)
        except Exception:
            self.show_alert(
                context=obj.context,
            )
