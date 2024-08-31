from pydantic import BaseModel


class SendToPropertyInspector(BaseModel):
    """
    The Property Inspector will receive a sendToPropertyInspector event when the plugin
    sends a sendToPropertyInspector event.

    action: The action's unique identifier.
    context: A value to identify the instance's action.
    payload: A JSON object
    event: sendToPropertyInspector

    https://docs.elgato.com/sdk/plugins/events-received#sendtopropertyinspector
    """
    action: str
    context: str
    payload: dict
    event: str = "sendToPropertyInspector"
