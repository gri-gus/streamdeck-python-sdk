from pydantic import BaseModel


class DidReceiveDeepLinkPayload(BaseModel):
    """
    url: The deep-link URL, with the prefix omitted. For example
        the URL streamdeck://plugins/message/com.elgato.test/hello-world would result in a url of hello-world.
    """
    url: str


class DidReceiveDeepLink(BaseModel):
    """
    ! Available from Stream Deck 6.5 onwards.

    Occurs when Stream Deck receives a deep-link message intended for the plugin.
    The message is re-routed to the plugin, and provided as part of the payload.
    One-way deep-link message can be routed to the plugin using the URL format:
    streamdeck://plugins/message/<PLUGIN_UUID>/{MESSAGE}

    event: didReceiveDeepLink
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#didreceivedeeplink
    """
    payload: DidReceiveDeepLinkPayload
    event: str = "didReceiveDeepLink"
