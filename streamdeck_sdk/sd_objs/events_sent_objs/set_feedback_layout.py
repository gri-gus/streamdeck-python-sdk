from pydantic import BaseModel


class SetFeedbackLayoutPayload(BaseModel):
    """
    layout: A predefined layout identifier or the relative path to a json file that contains a custom layout.
    """
    layout: str


class SetFeedbackLayout(BaseModel):
    """
    (SD+)
    The plugin can send a setFeedbackLayout event to the Stream Deck application to dynamically change the
    current Stream Deck + touch display layout. setFeedbackLayout can use the id of a built-in layout or
    a relative path to a custom layout JSON file. See Layouts for more information.

    event: setFeedbackLayout
    context: A value to Identify the instance's action you want to modify.
    payload: Json

    https://docs.elgato.com/sdk/plugins/events-sent#setfeedbacklayout-sd
    """
    context: str
    payload: SetFeedbackLayoutPayload
    event: str = "setFeedbackLayout"
