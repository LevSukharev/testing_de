from pydantic import BaseModel

class Street(BaseModel):
    number: int
    name: str
