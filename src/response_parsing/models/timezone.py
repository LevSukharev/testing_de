from pydantic import BaseModel

class Timezone(BaseModel):
    offset: str
    description: str