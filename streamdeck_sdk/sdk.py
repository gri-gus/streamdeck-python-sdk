import argparse
import json
import logging
from os import PathLike
from pathlib import Path
from typing import Optional, List, Dict, Set

from websockets.sync.server import (
    ServerConnection,
    WebSocketServer,  # noqa
    serve,
)

from .event_routing_mixin import EventRoutingMixin
from .logger import (
    init_root_logger,
    log_errors,
    rename_plugin_logger,
)
from .mixins import Base
from .sd_objs import registration_objs
from .simple_ws.client import WebSocketClientApp
from .utils.in_separate_thread import in_separate_thread

logger = logging.getLogger(__name__)


class Action(Base):
    UUID: str  # Required

    def __init__(self):
        self.plugin_uuid: Optional[str] = None
        self.ws: Optional[WebSocketClientApp] = None
        self.info: Optional[registration_objs.Info] = None


class StreamDeck(Base, EventRoutingMixin):
    def __init__(
            self,
            actions: Optional[List[Action]] = None,
            debug: bool = False,
            debug_port: int = 5581,
            *,
            log_file: Optional[PathLike] = None,
            log_level: int = logging.INFO,
            log_max_bytes: int = 3 * 1024 * 1024,  # 3 MB
            log_backup_count: int = 2,
    ):
        if log_file is not None:
            if debug:
                log_level = logging.DEBUG
            log_file: Path = Path(log_file)
            init_root_logger(
                log_file=log_file,
                log_level=log_level,
                log_max_bytes=log_max_bytes,
                log_backup_count=log_backup_count,
            )

        self.actions_list = actions
        self.actions: Dict[str, Action] = {}

        self.debug = debug
        self.debug_port = debug_port
        self.debug_clients: Set[ServerConnection] = set()

        self.ws: Optional[WebSocketClientApp] = None
        self.port: Optional[int] = None
        self.plugin_uuid: Optional[str] = None
        self.register_event: Optional[str] = None
        self.info: Optional[registration_objs.Info] = None

        self.registration_dict: Optional[dict] = None

    @log_errors
    def run(self):
        logger.debug(f"Plugin has been launched")

        if self.debug:
            self.run_debug()
            return

        self.__parse_args()
        self.ws = WebSocketClientApp(
            uri=f'ws://localhost:{self.port}/',
            on_message=self.ws_on_message,
            on_error=self.ws_on_error,
            on_close=self.ws_on_close,
            on_open=self.ws_on_open,
        )
        self.__init_actions()
        self.ws.run_forever()

    @log_errors
    def run_debug(self):
        logger.warning("Debug mode.")

        try:
            logger.info("Trying to connect to the debug server.")
            self.ws = WebSocketClientApp(
                uri=f'ws://localhost:{self.debug_port}/',
                on_message=self.ws_on_message,
            )
            logger.info(f"Successfully connected to the debug server.")
            self.__init_actions()
            self.ws.run_forever()
            return
        except Exception:
            logger.debug(f"Failed to connect to debug server.")

        logger.info("Trying to create a debug server.")
        self.__parse_args()
        self.__debug_server_run()
        logger.debug("Debug server is running.")
        self.ws = WebSocketClientApp(
            uri=f'ws://localhost:{self.port}/',
            on_message=self.__debug_server_on_message,
            on_open=self.ws_on_open,
        )
        logger.debug("Debug server connected to StreamDeck.")
        self.ws.run_forever()
        logger.info("Debug server stopped.")

    def __init_actions(self) -> None:
        if self.actions_list is None:
            return

        for action in self.actions_list:
            try:
                action_uuid = action.UUID
            except AttributeError:
                action_class = str(action.__class__)
                message = f"{action_class} must have attribute UUID."
                logger.error(message, exc_info=True)
                raise AttributeError(message)
            action.ws = self.ws
            action.plugin_uuid = self.plugin_uuid
            action.info = self.info
            self.actions[action_uuid] = action

    def __parse_args(self):
        parser = argparse.ArgumentParser(description='StreamDeck Plugin')
        parser.add_argument('-port', dest='port', type=int, help="Port", required=True)
        parser.add_argument('-pluginUUID', dest='pluginUUID', type=str, help="pluginUUID", required=True)
        parser.add_argument('-registerEvent', dest='registerEvent', type=str, help="registerEvent", required=True)
        parser.add_argument('-info', dest='info', type=str, help="info", required=True)
        args = parser.parse_args()
        logger.debug(f"{args=}")

        self.port = args.port
        self.plugin_uuid = args.pluginUUID
        self.register_event = args.registerEvent
        self.info = registration_objs.Info.parse_obj(json.loads(args.info))
        logger.debug(f"{self.info=}")

        rename_plugin_logger(name=self.info.plugin.uuid)

        self.registration_dict = {"event": self.register_event, "uuid": self.plugin_uuid}
        logger.debug(f"{self.registration_dict=}")

    @in_separate_thread(daemon=True)
    def __debug_server_run(self):
        server: WebSocketServer = serve(handler=self.__debug_server_handler, host="localhost", port=self.debug_port)
        server.serve_forever()

    def __debug_server_handler(self, websocket: ServerConnection):
        self.debug_clients.add(websocket)
        logger.debug(f"Client {websocket} added, clients: {self.debug_clients}.")
        try:
            for message in websocket:
                logger.debug(f"Message {message} received from StreamDeckPlugin.")
                self.ws.send(message)
                logger.debug(f"Message {message} sent to StreamDeck.")
        except Exception:  # noqa
            self.debug_clients.remove(websocket)
            logger.debug(f"Client {websocket} removed, clients: {self.debug_clients}")

    def __debug_server_on_message(
            self,
            ws: WebSocketClientApp,  # noqa
            message: str,
    ) -> None:
        logger.debug(f"Received message from StreamDeck. message={message}.")
        for client in self.debug_clients:
            client.send(message)
            logger.debug(f"Message sent to StreamDeckPlugin {client}. message={message}.")