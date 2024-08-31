from typing import Optional

from pydantic import BaseModel


class SetImagePayload(BaseModel):
    """
    image: The image to display encoded in base64 with the image format declared in the mime
        type (PNG, JPEG, BMP, ...). svg is also supported. If not provided, the image is
        reset to the default image from the manifest.
        You can use functions from image_converters.py for convert image in base64.
    target: Specify if you want to display the title on the hardware and software (0),
        only on the hardware (1), or only on the software (2). Default is 0.
    state: A 0-based integer value representing the state of an action with multiple states. If not specified,
        the image is set to all states.
    """
    image: str  # base64
    target: int = 0
    state: Optional[int] = None


class SetImage(BaseModel):
    """
    The plugin can send a setImage event to the Stream Deck application to dynamically change the image displayed
    by an instance of an action.

    event: setImage
    context: A value to Identify the instance's action you want to modify.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-sent#setimage
    """
    context: str
    payload: SetImagePayload
    event: str = "setImage"
