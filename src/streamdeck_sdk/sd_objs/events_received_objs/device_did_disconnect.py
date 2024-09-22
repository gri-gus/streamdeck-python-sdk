from pydantic import BaseModel


class DeviceDidDisconnect(BaseModel):
    """
    When a device is unplugged from the computer, the plugin will receive a deviceDidDisconnect event.

    event: deviceDidDisconnect
    device: A value to identify the device.

    https://docs.elgato.com/sdk/plugins/events-received#devicediddisconnect
    """
    device: str
    event: str = "deviceDidDisconnect"
