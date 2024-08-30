from pydantic import BaseModel


class PropertyInspectorDidAppear(BaseModel):
    """
    The plugin will receive a propertyInspectorDidAppear event when the Property Inspector appears.
    * This API has been introduced in Stream Deck 4.1.

    action: The action's unique identifier.
    event: propertyInspectorDidAppear
    context: A value to identify the instance's action.
    device: A value to identify the device.

    https://docs.elgato.com/sdk/plugins/events-received#propertyinspectordidappear
    """
    action: str
    context: str
    device: str
    event: str = "propertyInspectorDidAppear"
