from typing import Optional

from pydantic import BaseModel

from .assets.key_coordinates import KeyCoordinates


class KeyUpPayload(BaseModel):
    """
    settings: This JSON object contains data that you can set and is stored persistently.
    coordinates: The coordinates of the action triggered.
    state: Only set when the action has multiple states defined in its manifest.json. The 0-based value contains
        the current state of the action.
    userDesiredState: Only set when the action is triggered with a specific value from a Multi-Action. For
        example, if the user sets the Game Capture Record action to be disabled in a Multi-Action, you would see the
        value 1. 0 and 1 are valid.
    isInMultiAction: Boolean indicating if the action is inside a Multi-Action.
    """
    settings: dict
    isInMultiAction: bool
    state: Optional[int] = None
    coordinates: Optional[KeyCoordinates] = None
    userDesiredState: Optional[int] = None


class KeyUp(BaseModel):
    """
    When the user releases a key, the plugin will receive the keyUp event.

    action: The action's unique identifier. If your plugin supports multiple actions, you should use this value
        to find out which action was triggered.
    event: keyUp
    context: A value to identify the instance's action. You will need to pass this opaque value
        to several APIs like the setTitle API.
    device: A value to identify the device.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#keyup
    """
    action: str
    context: str
    device: str
    payload: KeyUpPayload
    event: str = "keyUp"
