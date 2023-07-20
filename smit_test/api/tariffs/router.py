import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import TypeAdapter
from tortoise.exceptions import IntegrityError
from tortoise.expressions import Q

from smit_test.api.deps import only_admin
from smit_test.api.schemas import Status

from .compute.router import compute_router
from .models import Tariffs
from .schemas import CreateTariffRequest, CreateTariffsRequest, ReadTariffResponse

tariffs_router = APIRouter(prefix="/tariffs")
tariffs_router.include_router(compute_router)

protected_route_deps = [Depends(only_admin)]


@tariffs_router.post("", dependencies=protected_route_deps)
async def create(data: CreateTariffsRequest) -> Status:
    tariffs = []
    for date, tariffs_detail in data.root.items():
        for tariff_detail in tariffs_detail:
            tariffs.append(
                Tariffs(
                    date=date,
                    cargo_type_id=tariff_detail.cargo_type,
                    rate=tariff_detail.rate,
                )
            )
    try:
        await Tariffs.bulk_create(tariffs)
    except IntegrityError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, "Some CargoType Does Not Exist"
        )
    return Status(message="Created")


@tariffs_router.get("")
async def list_(
    date: datetime.date | None = Query(None), cargo_type: str | None = Query(None)
) -> list[ReadTariffResponse]:
    qs = []
    if date:
        qs.append(Q(date=date))
    if cargo_type:
        qs.append(Q(cargo_type_id=cargo_type))
    tariffs = await Tariffs.filter(Q(*qs, join_type="AND")).all()
    return TypeAdapter(list[ReadTariffResponse]).validate_python(tariffs)


@tariffs_router.get("/{tariff_id}")
async def read(tariff_id: int) -> ReadTariffResponse:
    tariff = await Tariffs.get(id=tariff_id)
    return ReadTariffResponse.model_validate(tariff)


@tariffs_router.put("/{tariff_id}", dependencies=protected_route_deps)
async def update(tariff_id: int, data: CreateTariffRequest) -> ReadTariffResponse:
    try:
        await Tariffs.filter(id=tariff_id).update(**data.model_dump(by_alias=True))
    except IntegrityError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, f"CargoType {data.cargo_type} Does Not Exist"
        )
    tariff = await Tariffs.get(id=tariff_id)
    return ReadTariffResponse.model_validate(tariff)


@tariffs_router.delete("/{tariff_id}", dependencies=protected_route_deps)
async def delete(tariff_id: int) -> Status:
    deleted_count = await Tariffs.filter(id=tariff_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Tariff {tariff_id} not found")
    return Status(message=f"Deleted Tariff {tariff_id}")
