import logging
from typing import Callable, Optional

from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError, ConnectionClosed
from websockets.sync.client import ClientConnection, connect

logger = logging.getLogger('simple_ws_client')


class WebSocketClientApp:
    def __init__(
            self,
            uri: str,
            *,
            on_open: Callable = None,
            on_message: Callable = None,
            on_error: Callable = None,
            on_close: Callable = None,
    ):
        self.uri = uri
        self.on_open = on_open
        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close
        self.client: Optional[ClientConnection] = connect(uri=self.uri)

    def send(self, message):
        self.client.send(message=message)

    def close(self):
        self.client.close()

    def run_forever(self):
        self._callback(self.on_open)
        while True:
            try:
                message = self.client.recv()
                logger.debug(f"Message received. {message=}")
            except ConnectionClosedOK as err:
                self._handle_connection_close(err=err)
                break
            except ConnectionClosedError as err:
                self._callback(self.on_error, err)
                self._handle_connection_close(err=err)
                break
            self._callback(self.on_message, message)

    def _handle_connection_close(self, err: ConnectionClosed):
        close_status_code = getattr(err.rcvd, "code", None)
        close_msg = getattr(err.rcvd, "reason", None)
        self._callback(self.on_close, close_status_code, close_msg)

    def _callback(self, callback, *args):
        if not callback:
            return
        try:
            callback(self.client, *args)
        except Exception as err:
            logger.error(f"error from callback {callback}: {err}")
            if self.on_error:
                self.on_error(self, err)
