from pydantic import BaseModel


class SystemDidWakeUp(BaseModel):
    """
    When the computer wakes up, the plugin will receive the systemDidWakeUp event.
    Several important points to note:
    * A plugin could get multiple systemDidWakeUp events when waking up the computer
    * When the plugin receives the systemDidWakeUp event, there is no guarantee that the devices are available
    * This API has been introduced in Stream Deck 4.3.

    event: systemDidWakeUp

    https://docs.elgato.com/sdk/plugins/events-received#systemdidwakeup
    """
    event: str = "systemDidWakeUp"
