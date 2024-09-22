from pydantic import BaseModel


class GetSettings(BaseModel):
    """
    The plugin and Property Inspector can request the persistent data stored for the action's
    instance using the getSettings event.

    event: getSettings
    context: A value to Identify the instance's action or Property Inspector. In the case of
        the Property Inspector, this value is received by the Property Inspector as parameter of
        the connectElgatoStreamDeckSocket function.

    https://docs.elgato.com/sdk/plugins/events-sent#getsettings
    """
    context: str
    event: str = "getSettings"
