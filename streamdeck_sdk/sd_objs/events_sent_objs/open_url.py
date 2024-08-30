from pydantic import BaseModel


class OpenUrlPayload(BaseModel):
    """
    url: An URL to open in the default browser.
    """
    url: str


class OpenUrl(BaseModel):
    """
    The plugin and Property Inspector can tell the Stream Deck application to open URL in the
    default browser using the openUrl event.

    event: openUrl
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-sent#openurl
    """
    payload: OpenUrlPayload
    event: str = "openUrl"
