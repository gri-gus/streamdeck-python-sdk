from pydantic import BaseModel


class ShowOk(BaseModel):
    """
    The plugin can send a showOk event to the Stream Deck application to temporarily show an OK checkmark icon on
    the image displayed by an instance of an action.

    event: showOk
    context: A value to identify the instance's action.

    https://docs.elgato.com/sdk/plugins/events-sent#showok
    """
    context: str
    event: str = "showOk"
