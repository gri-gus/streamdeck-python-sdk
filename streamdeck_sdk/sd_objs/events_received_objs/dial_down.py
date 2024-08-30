from pydantic import BaseModel

from .assets.controller_enum import ControllerEnum
from .assets.key_coordinates import KeyCoordinates


class DialDownPayload(BaseModel):
    """
    settings: This JSON object contains data that you can set and are stored persistently.
    coordinates: The coordinates of the action triggered.
    controller: Encoder.
    """
    settings: dict
    coordinates: KeyCoordinates
    controller: ControllerEnum = ControllerEnum.ENCODER


class DialDown(BaseModel):
    """
    (SD+)
    When the user presses the encoder down, the plugin will receive the dialDown event (SD+).

    action: The action's unique identifier. If your plugin supports multiple actions,
        you should use this value to see which action was triggered.
    event: dialDown
    context: A value identifying the instance's action. You will need to pass this
        opaque value to several APIs like the setTitle API.
    device: A value to identify the device.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#dialdown-sd
    """
    action: str
    context: str
    device: str
    payload: DialDownPayload
    event: str = "dialDown"
