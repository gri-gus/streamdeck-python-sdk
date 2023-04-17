from typing import List, Optional

from pydantic import BaseModel


# region NestedModels
class InfoApplication(BaseModel):
    font: str
    language: str
    platform: str
    platformVersion: str
    version: str


class InfoPlugin(BaseModel):
    uuid: str
    version: str


class InfoColors(BaseModel):
    buttonPressedBackgroundColor: str
    buttonPressedBorderColor: str
    buttonPressedTextColor: str
    disabledColor: Optional[str]
    highlightColor: str
    mouseDownColor: Optional[str]


class InfoDeviceSize(BaseModel):
    columns: int
    rows: int


class InfoDevice(BaseModel):
    id: str
    name: str
    size: InfoDeviceSize
    type: int


# endregion NestedModels

# region Models
class Info(BaseModel):
    application: InfoApplication
    plugin: InfoPlugin
    devicePixelRatio: int
    colors: InfoColors
    devices: List[InfoDevice]

# endregion Models
