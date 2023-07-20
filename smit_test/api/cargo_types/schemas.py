from smit_test.api.schemas import BaseSchema


class CreateCargoTypeRequest(BaseSchema):
    title: str


class ReadCargoTypeResponse(CreateCargoTypeRequest):
    pass
