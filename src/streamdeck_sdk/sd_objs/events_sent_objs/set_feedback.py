from pydantic import BaseModel


class SetFeedback(BaseModel):
    """
    (SD+)
    The plugin can send a setFeedback event to the Stream Deck application to dynamically change properties of
    items on the Stream Deck + touch display layout.

    event: setFeedback
    context: A value to Identify the instance's action you want to modify.
    payload: A JSON object.
        key: The key is a name of the element in layout to be changed with given value.
        value: The value to be set in key named layout element

    https://docs.elgato.com/sdk/plugins/events-sent#setfeedback-sd
    """
    context: str
    payload: dict
    event: str = "setFeedback"
