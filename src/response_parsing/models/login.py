from pydantic import BaseModel, Field

class Login(BaseModel):
    uuid: str
    username: str
    password: str
    salt: str
    password_md5: str = Field(alias='md5')
    sha1: str
    sha256: str