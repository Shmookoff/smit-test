import datetime

from pydantic import Field, RootModel

from smit_test.api.schemas import BaseSchema


class CreateTariffsRequestDetails(BaseSchema):
    cargo_type: str
    rate: float


CreateTariffsRequest = RootModel[dict[datetime.date, list[CreateTariffsRequestDetails]]]


class CreateTariffRequest(CreateTariffsRequestDetails):
    cargo_type: str = Field(serialization_alias="cargo_type_id")
    date: datetime.date


class ReadTariffResponse(CreateTariffRequest):
    id: int
    cargo_type: str = Field(validation_alias="cargo_type_id")
