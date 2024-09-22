from pydantic import BaseModel


class SetStatePayload(BaseModel):
    """
    state: A 0-based integer value representing the state requested.
    """
    state: int


class SetState(BaseModel):
    """
    This function can be used by a plugin to dynamically change the state of an action supporting multiple states.

    event: setState
    context: A value to identify the instance's action.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-sent#setstate
    """
    context: str
    payload: SetStatePayload
    event: str = "setState"
