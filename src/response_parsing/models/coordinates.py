from pydantic import BaseModel

class Coordinates(BaseModel):
    latitude: str
    longitude: str