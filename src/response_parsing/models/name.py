from pydantic import BaseModel, Field
class Name(BaseModel):
    name_title: str = Field(alias='title')
    name_first: str = Field(alias='first')
    name_last: str = Field(alias='last')