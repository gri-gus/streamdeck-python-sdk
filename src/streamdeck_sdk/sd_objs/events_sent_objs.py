from typing import Optional

from pydantic import BaseModel


# region NestedModels
class OpenUrlPayload(BaseModel):
    url: str


class LogMessagePayload(BaseModel):
    message: str


class SetTitlePayload(BaseModel):
    title: str
    target: int
    state: Optional[int]


class SetImagePayload(BaseModel):
    image: str  # base64
    target: int
    state: Optional[int]


class SetStatePayload(BaseModel):
    state: int


class SwitchToProfilePayload(BaseModel):
    profile: str


class SetFeedbackLayoutPayload(BaseModel):
    layout: str


# endregion NestedModels

# region Models
class SetSettings(BaseModel):
    context: str
    payload: dict
    event: str = "setSettings"


class GetSettings(BaseModel):
    context: str
    event: str = "getSettings"


class SetGlobalSettings(BaseModel):
    context: str
    payload: dict
    event: str = "setGlobalSettings"


class GetGlobalSettings(BaseModel):
    context: str
    event: str = "getGlobalSettings"


class OpenUrl(BaseModel):
    payload: OpenUrlPayload
    event: str = "openUrl"


class LogMessage(BaseModel):
    payload: LogMessagePayload
    event: str = "logMessage"


class SetTitle(BaseModel):
    context: str
    payload: SetTitlePayload
    event: str = "setTitle"


class SetImage(BaseModel):
    context: str
    payload: SetImagePayload
    event: str = "setImage"


class SetFeedback(BaseModel):
    context: str
    payload: dict
    event: str = "setFeedback"


class SetFeedbackLayout(BaseModel):
    context: str
    payload: SetFeedbackLayoutPayload
    event: str = "setFeedbackLayout"


class ShowAlert(BaseModel):
    context: str
    event: str = "showAlert"


class ShowOk(BaseModel):
    context: str
    event: str = "showOk"


class SetState(BaseModel):
    context: str
    payload: SetStatePayload
    event: str = "setState"


class SwitchToProfile(BaseModel):
    device: str
    context: str
    payload: SwitchToProfilePayload
    event: str = "switchToProfile"


class SendToPropertyInspector(BaseModel):
    action: str
    context: str
    payload: dict
    event: str = "sendToPropertyInspector"


class SendToPlugin(BaseModel):
    action: str
    context: str
    payload: dict
    event: str = "sendToPlugin"

# endregion Models
