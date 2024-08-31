from pydantic import BaseModel


class SendToPlugin(BaseModel):
    """
    The Property Inspector can send a payload to the plugin using the sendToPlugin event.
    The plugin will receive asynchronously an event sendToPlugin.

    action: The action's unique identifier. If your plugin supports multiple actions, you should use this value to
        find out which action was triggered.
    event: sendToPlugin
    context: A value to Identify the Property Inspector. This value is received by the Property Inspector as parameter
        of the connectElgatoStreamDeckSocket function.
    payload: A JSON object that will be received by the plugin.

    https://docs.elgato.com/sdk/plugins/events-sent#sendtoplugin
    """
    action: str
    context: str
    payload: dict
    event: str = "sendToPlugin"
