from pydantic import BaseModel, Field, validator
from typing import Union
from src.userValidator import *
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
    password_validation: bool = False
    sha1: str
    sha256: str

    @staticmethod
    def validatePassword(password: str) -> bool:
        return (bool(re.search(r"[A-Z]", password)) and bool(
            re.search(r"[a-z]", password)) and bool(re.search(r"\d", password))
                and bool(re.search(r"[!\"#$%&'()*+,\- ./:;<=>?@\[\]^_`{|}~]", password)))


    @validator('password_validation', always=True)
    def validate_password(cls, v, values):
        password = values.get('password')
        if password is None:
            raise ValueError('Password is required')
        return cls.validatePassword(password)


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
    email_validation: bool = False

    @staticmethod
    def validateEmail(email: str) -> bool:
        return bool(re.search(r"\S{1,}@[a-z]{2,}.[a-z]{2,}", email))

    @validator('email_validation', always=True)
    def validate_email(cls, v, values):
        email = values.get('email')
        if email is None:
            raise ValueError('email is required')
        return cls.validateEmail(email)