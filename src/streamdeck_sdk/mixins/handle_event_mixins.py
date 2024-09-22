from ..sd_objs import events_received_objs


class BaseEventHandlerMixin:
    pass


class ActionEventHandlersMixin(BaseEventHandlerMixin):
    def on_did_receive_settings(self, obj: events_received_objs.DidReceiveSettings) -> None:
        pass

    def on_key_down(self, obj: events_received_objs.KeyDown) -> None:
        pass

    def on_key_up(self, obj: events_received_objs.KeyUp) -> None:
        pass

    def on_touch_tap(self, obj: events_received_objs.TouchTap) -> None:
        pass

    def on_dial_down(self, obj: events_received_objs.DialDown) -> None:
        pass

    def on_dial_up(self, obj: events_received_objs.DialUp) -> None:
        pass

    def on_dial_rotate(self, obj: events_received_objs.DialRotate) -> None:
        pass

    def on_will_appear(self, obj: events_received_objs.WillAppear) -> None:
        pass

    def on_did_receive_deep_link(self, obj: events_received_objs.DidReceiveDeepLink) -> None:
        pass

    def on_will_disappear(self, obj: events_received_objs.WillDisappear) -> None:
        pass

    def on_title_parameters_did_change(self, obj: events_received_objs.TitleParametersDidChange) -> None:
        pass

    def on_property_inspector_did_appear(self, obj: events_received_objs.PropertyInspectorDidAppear) -> None:
        pass

    def on_property_inspector_did_disappear(self, obj: events_received_objs.PropertyInspectorDidDisappear) -> None:
        pass

    def on_send_to_plugin(self, obj: events_received_objs.SendToPlugin) -> None:
        pass

    def on_send_to_property_inspector(self, obj: events_received_objs.SendToPropertyInspector) -> None:
        pass


class PluginEventHandlersMixin(BaseEventHandlerMixin):
    def on_did_receive_global_settings(self, obj: events_received_objs.DidReceiveGlobalSettings) -> None:
        pass

    def on_device_did_connect(self, obj: events_received_objs.DeviceDidConnect) -> None:
        pass

    def on_device_did_disconnect(self, obj: events_received_objs.DeviceDidDisconnect) -> None:
        pass

    def on_application_did_launch(self, obj: events_received_objs.ApplicationDidLaunch) -> None:
        pass

    def on_application_did_terminate(self, obj: events_received_objs.ApplicationDidTerminate) -> None:
        pass

    def on_system_did_wake_up(self, obj: events_received_objs.SystemDidWakeUp) -> None:
        pass
