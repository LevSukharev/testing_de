from pydantic import BaseModel

class Picture(BaseModel):
    large: str
    medium: str
    thumbnail: str