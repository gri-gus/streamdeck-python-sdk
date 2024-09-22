from pydantic import BaseModel


class ShowAlert(BaseModel):
    """
    The plugin can send a showAlert event to the Stream Deck application to temporarily show an alert icon on the
    image displayed by an instance of an action.

    event: showAlert
    context: A value to identify the instance's action.

    https://docs.elgato.com/sdk/plugins/events-sent#showalert
    """
    context: str
    event: str = "showAlert"
