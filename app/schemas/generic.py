from pydantic import BaseModel

class GenericIdSchema(BaseModel):
    id: int