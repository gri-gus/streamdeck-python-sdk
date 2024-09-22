from pydantic import BaseModel


class SwitchToProfilePayload(BaseModel):
    """
    profile: The name of the profile to switch to. The name should be identical to the name provided
        in the manifest.json file.
    page: Page to show when switching to the profile; indexed from 0.
    """
    profile: str
    page: int


class SwitchToProfile(BaseModel):
    """
    The plugin can tell the Stream Deck application to switch to one of his preconfigured read-only profile
    using the switchToProfile event.
    * Note that a plugin can only switch to read-only profiles declared in its manifest.json file. If the profile
    field is missing or empty, the Stream Deck application will switch to the previously selected profile.

    event: switchToProfile
    context: A value to Identify the plugin. This value should be set to the PluginUUID received during the
        registration procedure.
    device: A value to identify the device.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-sent#switchtoprofile
    """
    device: str
    context: str
    payload: SwitchToProfilePayload
    event: str = "switchToProfile"
