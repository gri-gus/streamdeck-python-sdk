import json
from typing import Union

import pydantic
import websocket
from websocket import ABNF

from . import events_received_objs
from . import events_sent_objs
from .logger import log_errors


class SendMixin:
    ws: websocket.WebSocketApp

    @log_errors
    def send(
            self,
            data: Union[pydantic.BaseModel, dict, str],
            opcode=ABNF.OPCODE_TEXT,
    ) -> None:
        if isinstance(data, pydantic.BaseModel):
            data = data.json(ensure_ascii=False)
        elif isinstance(data, dict):
            data = json.dumps(data, ensure_ascii=False)
        self.ws.send(data, opcode)


class EventsSentMixin(SendMixin):
    plugin_uuid: str

    def set_global_settings(self, payload: dict) -> None:
        message = events_sent_objs.SetGlobalSettings(
            context=self.plugin_uuid,
            payload=payload,
        ).json()
        self.send(message)

    def get_global_settings(self) -> None:
        message = events_sent_objs.GetGlobalSettings(
            context=self.plugin_uuid,
        ).json()
        self.send(message)

    def open_url(self, url: str) -> None:
        message = events_sent_objs.OpenUrl(
            payload=events_sent_objs.OpenUrlPayload(
                url=url,
            ),
        ).json()
        self.send(message)

    def log_message(self, message: str) -> None:
        message = events_sent_objs.LogMessage(
            payload=events_sent_objs.LogMessagePayload(
                message=message,
            ),
        ).json()
        self.send(message)


class ActionEventHandlersMixin:
    def on_did_receive_settings(self, obj: events_received_objs.DidReceiveSettings):
        pass

    def on_key_down(self, obj: events_received_objs.KeyDown):
        pass

    def on_key_up(self, obj: events_received_objs.KeyUp):
        pass

    def on_touch_tap(self, obj: events_received_objs.TouchTap):
        pass

    def on_dial_press(self, obj: events_received_objs.DialPress):
        pass

    def on_dial_rotate(self, obj: events_received_objs.DialRotate):
        pass

    def on_will_appear(self, obj: events_received_objs.WillAppear):
        pass

    def on_will_disappear(self, obj: events_received_objs.WillDisappear):
        pass

    def on_title_parameters_did_change(self, obj: events_received_objs.TitleParametersDidChange):
        pass

    def on_property_inspector_did_appear(self, obj: events_received_objs.PropertyInspectorDidAppear):
        pass

    def on_property_inspector_did_disappear(self, obj: events_received_objs.PropertyInspectorDidDisappear):
        pass

    def on_send_to_plugin(self, obj: events_received_objs.SendToPlugin):
        pass

    def on_send_to_property_inspector(self, obj: events_received_objs.SendToPropertyInspector):
        pass


class APIEventHandlersMixin:
    def on_did_receive_global_settings(self, obj: events_received_objs.DidReceiveGlobalSettings):
        pass

    def on_device_did_connect(self, obj: events_received_objs.DeviceDidConnect):
        pass

    def on_device_did_disconnect(self, obj: events_received_objs.DeviceDidDisconnect):
        pass

    def on_application_did_launch(self, obj: events_received_objs.ApplicationDidLaunch):
        pass

    def on_application_did_terminate(self, obj: events_received_objs.ApplicationDidTerminate):
        pass

    def on_system_did_wake_up(self, obj: events_received_objs.SystemDidWakeUp):
        pass
