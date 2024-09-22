from typing import Optional

from pydantic import BaseModel

from .assets.key_coordinates import KeyCoordinates


class KeyDownPayload(BaseModel):
    """
    settings: This JSON object contains data that you can set and are stored persistently.
    coordinates: The coordinates of the action triggered.
    state: Only set when the action has multiple states defined in its manifest.json. The 0-based value
        contains the current state of the action.
    userDesiredState: Only set when the action is triggered with a specific value from a
        Multi-Action. For example, if the user sets the Game Capture Record action to be disabled in
        a Multi-Action, you would see the value 1. 0 and 1 are valid.
    isInMultiAction: Boolean indicating if the action is inside a Multi-Action.
    """
    settings: dict
    isInMultiAction: bool
    coordinates: Optional[KeyCoordinates] = None
    state: Optional[int] = None
    userDesiredState: Optional[int] = None


class KeyDown(BaseModel):
    """
    When the user presses a key, the plugin will receive the keyDown event.

    action: The action's unique identifier. If your plugin supports multiple actions, you should use this value
        to see which action was triggered.
    event: keyDown
    context: A value identifying the instance's action. You will need to pass this opaque value to
        several APIs like the setTitle API.
    device: A value to identify the device.
    payload: A JSON object.

    https://docs.elgato.com/sdk/plugins/events-received#keydown
    """
    action: str
    context: str
    device: str
    payload: KeyDownPayload
    event: str = "keyDown"
