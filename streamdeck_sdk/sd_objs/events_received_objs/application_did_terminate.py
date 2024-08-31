from pydantic import BaseModel


class ApplicationDidTerminatePayload(BaseModel):
    """
    application: The identifier of the application that has been terminated.
    """
    application: str


class ApplicationDidTerminate(BaseModel):
    """
    A plugin can request in its manifest.json to be notified when some applications are launched
    or terminated. The manifest.json should contain an ApplicationsToMonitor
    object specifying the list of application identifiers to monitor. On macOS, the application bundle
    identifier is used while the exe filename is used on Windows.
    For example, the Apple Mail: "application": "com.apple.mail"

    event: applicationDidTerminate
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-received#applicationdidterminate
    """
    payload: ApplicationDidTerminatePayload
    event: str = "applicationDidTerminate"
