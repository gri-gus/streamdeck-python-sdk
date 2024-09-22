from typing import Optional

from pydantic import BaseModel

from .assets.controller_enum import ControllerEnum
from .assets.key_coordinates import KeyCoordinates


class WillAppearPayload(BaseModel):
    """
    settings: This JSON object contains data that you can set and are stored persistently.
    coordinates: The coordinates of the action triggered.
    controller: Defines the controller type the action is applicable to. Keypad refers to a standard action on
        a Stream Deck device, e.g. 1 of the 15 buttons on the Stream Deck MK.2, or a pedal on the
        Stream Deck Pedal, etc., whereas an Encoder refers to a dial / touchscreen on the Stream Deck+.
    state: Only set when the action has multiple states defined in its manifest.json. The 0-based value
        contains the current state of the action.
    isInMultiAction: Boolean indicating if the action is inside a Multi-Action.
    """
    settings: dict
    isInMultiAction: bool
    coordinates: Optional[KeyCoordinates] = None
    state: Optional[int] = None
    controller: Optional[ControllerEnum] = None


class WillAppear(BaseModel):
    """
    When an instance of an action is displayed on Stream Deck, for example, when the hardware is first plugged
    in or when a folder containing that action is entered, the plugin will receive a willAppear event. You will see
    such an event when:
    * the Stream Deck application is started
    * the user switches between profiles
    * the user sets a key to use your action

    action: The action's unique identifier. If your plugin supports multiple actions, you should use this value to
        know which action was triggered.
    event: willAppear
    context: A value to identify the instance's action. You will need to pass this opaque value to several APIs
        like the setTitle API.
    device: A value to identify the device.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#willappear
    """
    action: str
    context: str
    device: str
    payload: WillAppearPayload
    event: str = "willAppear"
