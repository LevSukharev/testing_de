from pydantic import BaseModel, Field, validator, field_validator, model_validator
from typing import Union
from src.validators import password_validate, email_validate


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

    @field_validator('password')
    def check_password(cls, v):
        if not v:
            raise ValueError('Password required')
        return v

    @model_validator(mode='after')
    def set_password_validation(cls, values):
        values.password_validation = password_validate(values.password)
        return values


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

    @field_validator('email')
    def check_email(cls, v):
        if not v:
            raise ValueError('Email required')
        return v

    @model_validator(mode='after')
    def set_email_validation(cls, values):
        values.email_validation = email_validate(values.email)
        return values
