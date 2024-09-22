from pydantic import BaseModel


class LogMessagePayload(BaseModel):
    """
    message: A string to write to the logs file.
    """
    message: str


class LogMessage(BaseModel):
    """
    The plugin and Property Inspector can use the logMessage event to write a debug message to the logs file.
    * Logs are saved to disk per plugin in the folder ~/Library/Logs/ElgatoStreamDeck/ on macOS
    and %appdata%\Elgato\StreamDeck\logs\ on Windows. Note that the log files are rotated each time
    the Stream Deck application is relaunched.

    event: logMessage
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-sent#logmessage
    """
    payload: LogMessagePayload
    event: str = "logMessage"
