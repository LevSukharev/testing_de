from pydantic import BaseModel, Field

from src.response_parsing.models.name import Name
from src.response_parsing.models.location import Location
from src.response_parsing.models.login import Login
from src.response_parsing.models.dob import Dob
from src.response_parsing.models.picture import Picture

class User(BaseModel):
   # user_id: int
    name: Name
    location: Location
    email: str
    login: Login
    dob: Dob
    phone: str
    cell: str
    picture: Picture
    nat: str
