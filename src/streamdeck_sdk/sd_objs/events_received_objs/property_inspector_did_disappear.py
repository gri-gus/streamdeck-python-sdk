from pydantic import BaseModel


class PropertyInspectorDidDisappear(BaseModel):
    """
    The plugin will receive a propertyInspectorDidDisappear event when the Property Inspector disappears.

    action: The action's unique identifier.
    event: propertyInspectorDidDisappear
    context: A value to identify the instance's action.
    device: A value to identify the device.

    https://docs.elgato.com/sdk/plugins/events-received#propertyinspectordiddisappear
    """
    action: str
    context: str
    device: str
    event: str = "propertyInspectorDidDisappear"
