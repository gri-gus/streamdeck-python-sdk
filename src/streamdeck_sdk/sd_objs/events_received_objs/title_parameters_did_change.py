from pydantic import BaseModel

from .assets.key_coordinates import KeyCoordinates


class TitleParametersDidChangePayloadTitleParameters(BaseModel):
    """
    fontFamily: The font family for the title.
    fontSize: The font size for the title.
    fontStyle: The font style for the title.
    fontUnderline: Boolean indicating an underline under the title.
    showTitle: Boolean indicating if the title is visible.
    titleAlignment: Vertical alignment of the title. Possible values are "top", "bottom" and "middle".
    titleColor: Title color.
    """
    fontFamily: str
    fontSize: int
    fontStyle: str
    fontUnderline: bool
    showTitle: bool
    titleAlignment: str
    titleColor: str


class TitleParametersDidChangePayload(BaseModel):
    """
    settings: This JSON object contains data that you can set and is stored persistently.
    coordinates: The coordinates of the action triggered.
    state: This value indicates which state of the action the title or title parameters have been changed.
    title: The new title.
    titleParameters: A JSON object describing the new title parameters.
    """
    coordinates: KeyCoordinates
    settings: dict
    state: int
    title: str
    titleParameters: TitleParametersDidChangePayloadTitleParameters


class TitleParametersDidChange(BaseModel):
    """
    When the user changes the title or title parameters of the instance of an action, the plugin will
    receive a titleParametersDidChange event.

    action: The action's unique identifier. If your plugin supports multiple actions, you should use this value
        to find out which action was triggered.
    event: titleParametersDidChange
    context: A value to identify the instance's action. You will need to pass this value to several APIs
        like the setTitle API.
    device: A value to identify the device.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#titleparametersdidchange
    """
    action: str
    context: str
    device: str
    payload: TitleParametersDidChangePayload
    event: str = "titleParametersDidChange"
