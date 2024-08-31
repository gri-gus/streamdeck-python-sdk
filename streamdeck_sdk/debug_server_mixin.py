import logging
from typing import Set

from websockets.sync.server import (
    ServerConnection,
    WebSocketServer,  # noqa
    serve,
)

from .mixins import SendMixin
from .simple_ws.client import WebSocketClientApp
from .utils.in_separate_thread import in_separate_thread

logger = logging.getLogger(__name__)


class DebugServerMixin(SendMixin):
    debug_clients: Set[ServerConnection]
    debug_port: int

    @in_separate_thread(daemon=True)
    def _debug_server_run(self):
        server: WebSocketServer = serve(
            handler=self._debug_server_handler,
            host="localhost",
            port=self.debug_port,
        )
        server.serve_forever()

    def _debug_server_handler(self, websocket: ServerConnection):
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

    def _debug_server_on_message(
            self,
            ws: WebSocketClientApp,  # noqa
            message: str,
    ) -> None:
        logger.debug(f"Received message from StreamDeck. message={message}.")
        for client in self.debug_clients:
            client.send(message)
            logger.debug(f"Message sent to StreamDeckPlugin {client}. message={message}.")
