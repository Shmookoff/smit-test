from pydantic import BaseModel, ConfigDict


class Status(BaseModel):
    message: str


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
