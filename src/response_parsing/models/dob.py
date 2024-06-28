from pydantic import BaseModel

class Dob(BaseModel):
    date: str
    age: int