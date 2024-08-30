from pydantic import BaseModel


class GetGlobalSettings(BaseModel):
    """
    The plugin and Property Inspector can request the persistent global data using the getGlobalSettings event.
    The plugin or Property Inspector will receive asynchronously an event didReceiveGlobalSettings the p
    containing the global settings.

    event: getGlobalSettings
    context: A value to Identify the plugin (inPluginUUID) or the Property Inspector (inPropertyInspectorUUID). This
        value is received during the Registration procedure.

    https://docs.elgato.com/sdk/plugins/events-sent#getglobalsettings
    """
    context: str
    event: str = "getGlobalSettings"
