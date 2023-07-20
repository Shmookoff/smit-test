import datetime

from fastapi import Query

from smit_test.api.schemas import BaseSchema


class ComputeRequestQuery(BaseSchema):
    cargo_type: str = Query()
    date: datetime.date = Query()
    declared_value: float = Query()


class ComputeResponse(BaseSchema):
    delivery_cost: float
