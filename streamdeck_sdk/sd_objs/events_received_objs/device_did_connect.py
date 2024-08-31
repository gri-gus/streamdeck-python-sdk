from pydantic import BaseModel


class DeviceDidConnectDeviceInfoSize(BaseModel):
    """
    The number of columns and rows of keys that the device owns.
    """
    columns: int
    rows: int


class DeviceDidConnectDeviceInfo(BaseModel):
    """
    type: Type of device. Possible values are kESDSDKDeviceType_StreamDeck (0),
        kESDSDKDeviceType_StreamDeckMini (1), kESDSDKDeviceType_StreamDeckXL (2),
        kESDSDKDeviceType_StreamDeckMobile (3) and kESDSDKDeviceType_CorsairGKeys (4).
    size: The number of columns and rows of keys that the device owns.
    name: The name of the device set by the user.
    """
    name: str
    type: int
    size: DeviceDidConnectDeviceInfoSize


class DeviceDidConnect(BaseModel):
    """
    When a device is plugged into the computer, the plugin will receive a deviceDidConnect event.

    event: deviceDidConnect
    device: A value to identify the device.
    deviceInfo: A JSON object containing information about the device.

    https://docs.elgato.com/sdk/plugins/events-received#devicedidconnect
    """
    device: str
    deviceInfo: DeviceDidConnectDeviceInfo
    event: str = "deviceDidConnect"
