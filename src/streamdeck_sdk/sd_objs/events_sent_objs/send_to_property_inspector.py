from pydantic import BaseModel


class SendToPropertyInspector(BaseModel):
    """
    The plugin can send a payload to the Property Inspector using the sendToPropertyInspector event.
    The Property Inspector will receive asynchronously an event sendToPropertyInspector.

    action: The action's unique identifier.
    event: sendToPropertyInspector
    context: A value to identify the instance's action.
    payload: A JSON object that will be received by the Property Inspector.

    https://docs.elgato.com/sdk/plugins/events-sent#sendtopropertyinspector
    """
    action: str
    context: str
    payload: dict
    event: str = "sendToPropertyInspector"
