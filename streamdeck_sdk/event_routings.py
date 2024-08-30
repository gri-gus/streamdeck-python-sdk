from enum import Enum
from typing import Type, Dict, get_type_hints

from pydantic import BaseModel

from . import mixins


class EventRoutingObjTypes(Enum):
    ACTION = "ACTION"
    PLUGIN = "PLUGIN"


class EventRoutingObj(BaseModel):
    handler_name: str
    obj_type: Type[BaseModel]
    type: EventRoutingObjTypes


EVENT_ROUTING_MAP: Dict[str, EventRoutingObj] = {}


def fill_routing_map(
        routing_map: Dict[str, EventRoutingObj],
        event_handler_mixin: mixins.BaseEventHandlerMixin,
        event_routing_obj_type: EventRoutingObjTypes,
) -> None:
    event_handler_mixin_dict = dict(event_handler_mixin.__dict__)
    for attr, value in event_handler_mixin_dict.items():
        attr: str
        if not attr.startswith("on_"):
            continue
        assert callable(value)

        handler_type_hints = get_type_hints(value)
        obj_type = handler_type_hints["obj"]
        obj = obj_type.construct()
        event_name = obj.event
        handler_name = value.__name__
        routing_map[event_name] = EventRoutingObj(
            handler_name=handler_name,
            obj_type=obj_type,
            type=event_routing_obj_type,
        )


def fill_event_routing_map() -> None:
    for event_handler_mixin, event_routing_obj_type in (
            (mixins.ActionEventHandlersMixin, EventRoutingObjTypes.ACTION),
            (mixins.PluginEventHandlersMixin, EventRoutingObjTypes.PLUGIN),
    ):
        fill_routing_map(
            routing_map=EVENT_ROUTING_MAP,
            event_handler_mixin=event_handler_mixin,
            event_routing_obj_type=event_routing_obj_type,
        )


fill_event_routing_map()
