from pydantic import BaseModel


class SetSettings(BaseModel):
    """
    The plugin and Property Inspector can save data persistently for the action's instance using the setSettings event.
    Note that when the plugin uses this API, the Property Inspector will automatically receive a didReceiveSettings
    callback with the new settings. Similarly, when the Property Inspector uses this API, the plugin will
    automatically receive a didReceiveSettings callback with the new settings.
    The setSettings API is available since Stream Deck 4.0 for the plugin. Starting
    with Stream Deck 4.1, this API is available from the Property Inspector.

    event: setSettings
    context: A value to Identify the instance's action or Property Inspector. This value is received by
        the Property Inspector as a parameter of the connectElgatoStreamDeckSocket function.
    payload: A JSON object which is persistently saved for the action's instance.

    https://docs.elgato.com/sdk/plugins/events-sent#setsettings
    """
    context: str
    payload: dict
    event: str = "setSettings"
