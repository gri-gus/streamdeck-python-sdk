from pydantic import BaseModel


class KeyCoordinates(BaseModel):
    """
    The coordinates of the action triggered.
    """
    column: int
    row: int
