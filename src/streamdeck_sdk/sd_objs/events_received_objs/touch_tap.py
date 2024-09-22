from typing import Tuple

from pydantic import BaseModel

from .assets.controller_enum import ControllerEnum
from .assets.key_coordinates import KeyCoordinates


class TouchTapPayload(BaseModel):
    """
    settings: This JSON object contains data that you can set and are stored persistently.
    controller: Encoder.
    coordinates: The coordinates of the action triggered.
    tapPos: The array which holds (x, y) coordinates as a position of tap inside of LCD slot associated with action.
    hold: Boolean which is true when long tap happened
    """
    settings: dict
    coordinates: KeyCoordinates
    tapPos: Tuple[int, int]
    hold: bool
    controller: ControllerEnum = ControllerEnum.ENCODER


class TouchTap(BaseModel):
    """
    (SD+)
    When the user touches the display, the plugin will receive the touchTap event.

    action: The action's unique identifier. If your plugin supports multiple actions,
        you should use this value to see which action was triggered.
    event: touchTap
    context: A value identifying the instance's action. You will need to pass this opaque
        value to several APIs like the setTitle API.
    device: A value to identify the device.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#touchtap-sd
    """
    action: str
    context: str
    device: str
    payload: TouchTapPayload
    event: str = "touchTap"
