from pydantic import BaseModel, Field
from typing import Union
class Name(BaseModel):
    name_title: str = Field(alias='title')
    name_first: str = Field(alias='first')
    name_last: str = Field(alias='last')

class Street(BaseModel):
    number: int
    name: str

class Coordinates(BaseModel):
    latitude: str
    longitude: str

class Timezone(BaseModel):
    offset: str
    description: str

class Location(BaseModel):
    street: Street
    city: str
    state: str
    country: str
    postcode: Union[str, int]
    coordinates: Coordinates
    timezone: Timezone

class Login(BaseModel):
    uuid: str
    username: str
    password: str
    salt: str
    password_md5: str = Field(alias='md5')
    sha1: str
    sha256: str

class Dob(BaseModel):
    date: str
    age: int

class Picture(BaseModel):
    large: str
    medium: str
    thumbnail: str

class User(BaseModel):
    gender: str
    name: Name
    location: Location
    email: str
    login: Login
    dob: Dob
    phone: str
    cell: str
    picture: Picture
    nat: str
