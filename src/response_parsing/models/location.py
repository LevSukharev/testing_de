from pydantic import BaseModel, Field
from typing import Union


from src.response_parsing.models.street import Street
from src.response_parsing.models.timezone import Timezone
from src.response_parsing.models.coordinates import Coordinates
class Location(BaseModel):
    street: Street
    city: str
    state: str
    country: str
    postcode: Union[str, int]
    coordinates: Coordinates
    timezone: Timezone

"""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_postcode

    @classmethod
    def validate_postcode(cls, v):
        if isinstance(v, int):
            return str(v)
        return v
"""