from typing import Optional

from pydantic import BaseModel


class SetTitlePayload(BaseModel):
    """
    title: The title to display. If there is no title parameter, the title is reset to the title set by the user.
    target: Specify if you want to display the title on the hardware and software (0), only on the hardware (1),
        or only on the software (2). Default is 0.
    state: A 0-based integer value representing the state of an action with multiple states. If not specified,
        the title is set to all states.
    """
    title: str
    target: int = 0
    state: Optional[int] = None


class SetTitle(BaseModel):
    """
    The plugin can send a setTitle event to the Stream Deck application to dynamically change the title
    displayed by an instance of an action.
    * Note: Show the title on your hardware or software using the Show Title checkbox in the Stream Deck window.

    event: setTitle
    context: A value to Identify the instance's action you want to modify.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-sent#settitle
    """
    context: str
    payload: SetTitlePayload
    event: str = "setTitle"
