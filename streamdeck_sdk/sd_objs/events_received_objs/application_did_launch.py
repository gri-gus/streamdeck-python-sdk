from pydantic import BaseModel


class ApplicationDidLaunchPayload(BaseModel):
    """
    application: The identifier of the application that has been launched.
    """
    application: str


class ApplicationDidLaunch(BaseModel):
    """
    A plugin can request in its manifest.json to be notified when some applications are launched or
    terminated. The manifest.json should contain an ApplicationsToMonitor object specifying the list of
    application identifiers to monitor. On macOS, the application bundle identifier is used while the exe
    filename is used on Windows.
    For example, the Apple Mail: "application": "com.apple.mail"

    event: applicationDidLaunch
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#applicationdidlaunch
    """
    payload: ApplicationDidLaunchPayload
    event: str = "applicationDidLaunch"
