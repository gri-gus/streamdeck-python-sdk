from enum import Enum
from typing import Optional

from pydantic import BaseModel


# region NestedModels
class ControllerEnum(str, Enum):
    KEYPAD = "Keypad"
    ENCODER = "Encoder"


class KeyCoordinates(BaseModel):
    column: int
    row: int


class KeyDownPayload(BaseModel):
    settings: dict
    coordinates: Optional[KeyCoordinates]
    state: Optional[int]
    userDesiredState: Optional[int]
    isInMultiAction: bool


class KeyUpPayload(BaseModel):
    settings: dict
    coordinates: Optional[KeyCoordinates]
    state: Optional[int]
    userDesiredState: Optional[int]
    isInMultiAction: bool


class WillAppearPayload(BaseModel):
    settings: dict
    coordinates: Optional[KeyCoordinates]
    state: Optional[int]
    isInMultiAction: bool
    controller: Optional[ControllerEnum]


class WillDisappearPayload(BaseModel):
    settings: dict
    coordinates: Optional[KeyCoordinates]
    state: Optional[int]
    isInMultiAction: bool
    controller: Optional[ControllerEnum]


class DidReceiveSettingsPayload(BaseModel):
    settings: dict
    coordinates: KeyCoordinates
    state: Optional[int]
    isInMultiAction: bool


class DidReceiveGlobalSettingsPayload(BaseModel):
    settings: dict


class TitleParametersDidChangePayloadTitleParameters(BaseModel):
    fontFamily: str
    fontSize: int
    fontStyle: str
    fontUnderline: bool
    showTitle: bool
    titleAlignment: str
    titleColor: str


class TitleParametersDidChangePayload(BaseModel):
    coordinates: KeyCoordinates
    settings: dict
    state: int
    title: str
    titleParameters: TitleParametersDidChangePayloadTitleParameters


class ApplicationDidTerminatePayload(BaseModel):
    application: str


class ApplicationDidLaunchPayload(BaseModel):
    application: str


class DeviceDidConnectDeviceInfoSize(BaseModel):
    columns: int
    rows: int


class DeviceDidConnectDeviceInfo(BaseModel):
    name: str
    type: int
    size: DeviceDidConnectDeviceInfoSize


class DialRotatePayload(BaseModel):
    settings: dict
    coordinates: KeyCoordinates
    ticks: int
    pressed: bool


class DialPressPayload(BaseModel):
    settings: dict
    coordinates: KeyCoordinates
    pressed: bool


class TouchTapPayload(BaseModel):
    settings: dict
    coordinates: KeyCoordinates
    tapPos: list
    hold: bool


class DialDownPayload(BaseModel):
    controller: str
    settings: dict
    coordinates: KeyCoordinates


class DialUpPayload(BaseModel):
    controller: str
    settings: dict
    coordinates: KeyCoordinates


# endregion NestedModels

# region Models
class DidReceiveSettings(BaseModel):
    action: str
    context: str
    device: str
    payload: DidReceiveSettingsPayload
    event: str = "didReceiveSettings"


class DidReceiveGlobalSettings(BaseModel):
    payload: DidReceiveGlobalSettingsPayload
    event: str = "didReceiveGlobalSettings"


class KeyDown(BaseModel):
    action: str
    context: str
    device: str
    payload: KeyDownPayload
    event: str = "keyDown"


class KeyUp(BaseModel):
    action: str
    context: str
    device: str
    payload: KeyUpPayload
    event: str = "keyUp"


class TouchTap(BaseModel):
    action: str
    context: str
    device: str
    payload: TouchTapPayload
    event: str = "touchTap"


class DialDown(BaseModel):
    action: str
    context: str
    device: str
    payload: DialDownPayload
    event: str = "dialDown"


class DialUp(BaseModel):
    action: str
    context: str
    device: str
    payload: DialUpPayload
    event: str = "dialUp"


class DialPress(BaseModel):
    action: str
    context: str
    device: str
    payload: DialPressPayload
    event: str = "dialPress"


class DialRotate(BaseModel):
    action: str
    context: str
    device: str
    payload: DialRotatePayload
    event: str = "dialRotate"


class WillAppear(BaseModel):
    action: str
    context: str
    device: str
    payload: WillAppearPayload
    event: str = "willAppear"


class WillDisappear(BaseModel):
    action: str
    context: str
    device: str
    payload: WillDisappearPayload
    event: str = "willDisappear"


class TitleParametersDidChange(BaseModel):
    action: str
    context: str
    device: str
    payload: TitleParametersDidChangePayload
    event: str = "titleParametersDidChange"


class DeviceDidConnect(BaseModel):
    device: str
    deviceInfo: DeviceDidConnectDeviceInfo
    event: str = "deviceDidConnect"


class DeviceDidDisconnect(BaseModel):
    device: str
    event: str = "deviceDidDisconnect"


class ApplicationDidLaunch(BaseModel):
    payload: ApplicationDidLaunchPayload
    event: str = "applicationDidLaunch"


class ApplicationDidTerminate(BaseModel):
    payload: ApplicationDidTerminatePayload
    event: str = "applicationDidTerminate"


class SystemDidWakeUp(BaseModel):
    event: str = "systemDidWakeUp"


class PropertyInspectorDidAppear(BaseModel):
    action: str
    context: str
    device: str
    event: str = "propertyInspectorDidAppear"


class PropertyInspectorDidDisappear(BaseModel):
    action: str
    context: str
    device: str
    event: str = "propertyInspectorDidDisappear"


class SendToPlugin(BaseModel):
    action: str
    context: str
    payload: dict
    event: str = "sendToPlugin"


class SendToPropertyInspector(BaseModel):
    action: str
    context: str
    payload: dict
    event: str = "sendToPropertyInspector"

# endregion Models
