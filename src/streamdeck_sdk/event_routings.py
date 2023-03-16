from dataclasses import dataclass
from typing import Type, Dict

import pydantic

from . import events_received_objs


@dataclass
class EventRoutingObj:
    handler_name: str
    obj: Type[pydantic.BaseModel]


ACTION_EVENT_ROUTING_MAP: Dict[str, EventRoutingObj] = {
    "didReceiveSettings": EventRoutingObj(
        obj=events_received_objs.DidReceiveSettings,
        handler_name="on_did_receive_settings",
    ),
    "keyDown": EventRoutingObj(
        obj=events_received_objs.KeyDown,
        handler_name="on_key_down",
    ),
    "keyUp": EventRoutingObj(
        obj=events_received_objs.KeyUp,
        handler_name="on_key_up",
    ),
    "touchTap": EventRoutingObj(
        obj=events_received_objs.TouchTap,
        handler_name="on_touch_tap",
    ),
    "dialPress": EventRoutingObj(
        obj=events_received_objs.DialPress,
        handler_name="on_dial_press",
    ),
    "dialRotate": EventRoutingObj(
        obj=events_received_objs.DialRotate,
        handler_name="on_dial_rotate",
    ),
    "willAppear": EventRoutingObj(
        obj=events_received_objs.WillAppear,
        handler_name="on_will_appear",
    ),
    "willDisappear": EventRoutingObj(
        obj=events_received_objs.WillDisappear,
        handler_name="on_will_disappear",
    ),
    "titleParametersDidChange": EventRoutingObj(
        obj=events_received_objs.TitleParametersDidChange,
        handler_name="on_title_parameters_did_change",
    ),
    "propertyInspectorDidAppear": EventRoutingObj(
        obj=events_received_objs.PropertyInspectorDidAppear,
        handler_name="on_property_inspector_did_appear",
    ),
    "propertyInspectorDidDisappear": EventRoutingObj(
        obj=events_received_objs.PropertyInspectorDidDisappear,
        handler_name="on_property_inspector_did_disappear",
    ),
    "sendToPlugin": EventRoutingObj(
        obj=events_received_objs.SendToPlugin,
        handler_name="on_send_to_plugin",
    ),
    "sendToPropertyInspector": EventRoutingObj(
        obj=events_received_objs.SendToPropertyInspector,
        handler_name="on_send_to_property_inspector",
    ),
}

PLUGIN_EVENT_ROUTING_MAP: Dict[str, EventRoutingObj] = {
    "didReceiveGlobalSettings": EventRoutingObj(
        obj=events_received_objs.DidReceiveGlobalSettings,
        handler_name="on_did_receive_global_settings",
    ),
    "deviceDidConnect": EventRoutingObj(
        obj=events_received_objs.DeviceDidConnect,
        handler_name="on_device_did_connect",
    ),
    "deviceDidDisconnect": EventRoutingObj(
        obj=events_received_objs.DeviceDidDisconnect,
        handler_name="on_device_did_disconnect",
    ),
    "applicationDidLaunch": EventRoutingObj(
        obj=events_received_objs.ApplicationDidLaunch,
        handler_name="on_application_did_launch",
    ),
    "applicationDidTerminate": EventRoutingObj(
        obj=events_received_objs.ApplicationDidTerminate,
        handler_name="on_application_did_terminate",
    ),
    "systemDidWakeUp": EventRoutingObj(
        obj=events_received_objs.SystemDidWakeUp,
        handler_name="on_system_did_wake_up",
    ),
}

EVENT_ROUTING_MAP: Dict[str, EventRoutingObj] = {
    **ACTION_EVENT_ROUTING_MAP,
    **PLUGIN_EVENT_ROUTING_MAP,
}
