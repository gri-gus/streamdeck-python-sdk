from pydantic import BaseModel

from .assets.controller_enum import ControllerEnum
from .assets.key_coordinates import KeyCoordinates


class DialRotatePayload(BaseModel):
    """
    settings: This JSON object contains data that you can set and are stored persistently.
    controller: Encoder.
    coordinates: The coordinates of the action triggered.
    ticks: The integer which holds the number of "ticks" on encoder rotation. Positive values are for clockwise
    rotation, negative values are for counterclockwise rotation, zero value is never happen.
    pressed: Boolean which is true on rotation when encoder pressed.
    """
    settings: dict
    coordinates: KeyCoordinates
    ticks: int
    pressed: bool
    controller: ControllerEnum = ControllerEnum.ENCODER


class DialRotate(BaseModel):
    """
    (SD+)
    When the user rotates the encoder, the plugin will receive the dialRotate event.

    action: The action's unique identifier. If your plugin supports multiple actions, you should use this value
    to see which action was triggered.
    event: dialRotate
    context: A value identifying the instance's action. You will need to pass this opaque value to
    several APIs like the setTitle API.
    device: A value to identify the device.
    payload: A JSON object.

    https://docs.elgato.com/sdk/plugins/events-received#dialrotate-sd
    """
    action: str
    context: str
    device: str
    payload: DialRotatePayload
    event: str = "dialRotate"
