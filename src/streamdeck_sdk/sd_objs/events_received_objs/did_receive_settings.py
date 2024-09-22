from typing import Optional

from pydantic import BaseModel

from .assets.key_coordinates import KeyCoordinates


class DidReceiveSettingsPayload(BaseModel):
    """
    settings: This JSON object contains persistently stored data.
    coordinates: The coordinates of the action triggered.
    state: Only set when the action has multiple states defined in its manifest.json. The 0-based
        value contains the current state of the action.
    isInMultiAction: Boolean indicating if the action is inside a Multi-Action.
    """
    settings: dict
    coordinates: KeyCoordinates
    isInMultiAction: bool
    state: Optional[int] = None


class DidReceiveSettings(BaseModel):
    """
    The didReceiveSettings event is received after calling the getSettings API
    to retrieve the persistent data stored for the action.

    action: The action's unique identifier.
    event: didReceiveSettings
    context: A value identifying the instance's action.
    device: A value to identify the device.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#didreceivesettings
    """
    action: str
    context: str
    device: str
    payload: DidReceiveSettingsPayload
    event: str = "didReceiveSettings"
