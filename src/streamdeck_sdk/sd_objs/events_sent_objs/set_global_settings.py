from pydantic import BaseModel


class SetGlobalSettings(BaseModel):
    """
    The plugin and Property Inspector can save persistent data globally. The data
    will be saved securely to the Keychain on macOS and the Credential Store on Windows. This API can
    be used to save tokens that should be available to every action in the plugin.
    Note that when the plugin uses this API, the Property Inspector will automatically receive
    a didReceiveGlobalSettings callback with the new settings. Similarly, when the Property Inspector uses
    this API, the plugin will automatically receive a didReceiveGlobalSettings callback with the new settings.
    This API has been introduced in Stream Deck 4.1.

    event: setGlobalSettings
    context: A value to Identify the plugin (inPluginUUID) or the Property Inspector (inPropertyInspectorUUID). This
        value is received during the Registration procedure.
    payload: A JSON object which is persistently saved globally.

    https://docs.elgato.com/sdk/plugins/events-sent#setglobalsettings
    """
    context: str
    payload: dict
    event: str = "setGlobalSettings"
