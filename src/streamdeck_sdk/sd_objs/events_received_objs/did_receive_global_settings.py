from pydantic import BaseModel


class DidReceiveGlobalSettingsPayload(BaseModel):
    settings: dict


class DidReceiveGlobalSettings(BaseModel):
    """
    The didReceiveGlobalSettings event is received after calling the getGlobalSettings API
    to retrieve the global persistent data stored for the plugin.

    event: didReceiveGlobalSettings
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#didreceiveglobalsettings
    """
    payload: DidReceiveGlobalSettingsPayload
    event: str = "didReceiveGlobalSettings"
