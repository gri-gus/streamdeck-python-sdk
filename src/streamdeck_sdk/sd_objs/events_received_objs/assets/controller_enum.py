from enum import Enum


class ControllerEnum(str, Enum):
    """
    Types of controller.
    """
    KEYPAD = "Keypad"
    ENCODER = "Encoder"
