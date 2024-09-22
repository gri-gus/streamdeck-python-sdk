from pydantic import BaseModel


class SendToPlugin(BaseModel):
    """
    The plugin will receive a sendToPlugin event when the Property Inspector sends a sendToPlugin event.

    action: The action's unique identifier.
    context: A value to identify the instance's action.
    payload: A JSON object
    event: sendToPlugin

    https://docs.elgato.com/sdk/plugins/events-received#sendtoplugin
    """
    action: str
    context: str
    payload: dict
    event: str = "sendToPlugin"
