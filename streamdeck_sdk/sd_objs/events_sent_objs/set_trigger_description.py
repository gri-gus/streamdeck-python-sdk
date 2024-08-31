from typing import Optional

from pydantic import BaseModel


class SetTriggerDescriptionPayload(BaseModel):
    """
    longTouch: Optional value that describes the long-touch interaction with the touch display. When undefined the
        description will be hidden.
    push: Optional value that describes the push interaction with the dial. When undefined the description will
        be hidden.
    rotate: Optional value that describes the rotate interaction with the dial. When undefined the description will
        be hidden.
    touch: Optional value that describes the touch interaction with the touch display. When undefined the description
        will be hidden.
    """
    longTouch: Optional[str] = None
    push: Optional[str] = None
    rotate: Optional[str] = None
    touch: Optional[str] = None


class SetTriggerDescription(BaseModel):
    """
    (SD+)
    Sets the trigger descriptions associated with an encoder (touch display + dial) action instance. All descriptions
    are optional; when one or more descriptions are defined all descriptions are updated, with undefined values
    having their description hidden in Stream Deck. To reset the descriptions to the default values defined
    within the manifest, an empty payload can be sent as part of the event.

    event: setTriggerDescription
    context: A value to identify the instance's action.
    payload: A JSON object

    https://docs.elgato.com/sdk/plugins/events-sent#settriggerdescription-sd
    """
    context: str
    payload: SetTriggerDescriptionPayload
    event: str = "setTriggerDescription"
