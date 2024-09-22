from typing import List, Optional

from pydantic import BaseModel


# region NestedModels
class InfoApplication(BaseModel):
    """
    language: In which language the Stream Deck application is running. Possible values are en, fr, de, es, ja, zh_CN.
    platform: On which platform the Stream Deck application is running. Possible values
        are kESDSDKApplicationInfoPlatformMac ("mac") and kESDSDKApplicationInfoPlatformWindows ("windows").
    version: The Stream Deck application version.
    platformVersion: The operating system version.
    """
    font: str
    language: str
    platform: str
    platformVersion: str
    version: str


class InfoPlugin(BaseModel):
    """
    version: The plugin version as written in the manifest.json.
    uuid: The unique identifier of the plugin.
    """
    uuid: str
    version: str


class InfoColors(BaseModel):
    """
    A JSON object containing information about the preferred user colors.
    """
    buttonPressedBackgroundColor: str
    buttonPressedBorderColor: str
    buttonPressedTextColor: str
    highlightColor: str
    disabledColor: Optional[str] = None
    mouseDownColor: Optional[str] = None


class InfoDeviceSize(BaseModel):
    """
    The number of columns and rows of keys that the device owns.
    """
    columns: int
    rows: int


class InfoDevice(BaseModel):
    """
    id: A value to identify the device.
    type: Type of device. Possible values are kESDSDKDeviceType_StreamDeck (0), kESDSDKDeviceType_StreamDeckMini (1),
        kESDSDKDeviceType_StreamDeckXL (2), kESDSDKDeviceType_StreamDeckMobile (3), kESDSDKDeviceType_CorsairGKeys (4),
        kESDSDKDeviceType_StreamDeckPedal (5), kESDSDKDeviceType_CorsairVoyager (6),
        and kESDSDKDeviceType_StreamDeckPlus (7).
    size: The number of columns and rows of keys that the device owns.
    name: The name of the device set by the user.
    """
    id: str
    name: str
    size: InfoDeviceSize
    type: int


# endregion NestedModels

# region Models
class Info(BaseModel):
    """
    The info parameter used in the registration process is A JSON object.

    application: A JSON object containing information about the application.
    plugin: A JSON object containing information about the plugin.
    devices: A JSON array containing information about the devices.
    devicePixelRatio: Pixel ratio value to indicate if the Stream Deck application is running on a HiDPI screen.
    colors: A JSON object containing information about the preferred user colors.

    https://docs.elgato.com/sdk/plugins/registration-procedure#info-parameter
    """
    application: InfoApplication
    plugin: InfoPlugin
    devicePixelRatio: int
    colors: InfoColors
    devices: List[InfoDevice]
# endregion Models
