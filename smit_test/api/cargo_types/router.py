from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from smit_test.api.deps import only_admin
from smit_test.api.schemas import Status

from .models import CargoTypes
from .schemas import CreateCargoTypeRequest, ReadCargoTypeResponse

cargo_types_router = APIRouter(prefix="/cargo_types")

protected_route_deps = [Depends(only_admin)]


@cargo_types_router.post("", dependencies=protected_route_deps)
async def create(data: CreateCargoTypeRequest) -> ReadCargoTypeResponse:
    cargo_type = await CargoTypes.create(**data.model_dump())
    return ReadCargoTypeResponse.model_validate(cargo_type)


@cargo_types_router.get("")
async def list_() -> list[ReadCargoTypeResponse]:
    cargo_types = await CargoTypes.all()
    return TypeAdapter(list[ReadCargoTypeResponse]).validate_python(
        cargo_types, from_attributes=True
    )


@cargo_types_router.get("/{cargo_type_title}")
async def read(cargo_type_title: str) -> ReadCargoTypeResponse:
    cargo_type = await CargoTypes.get(title=cargo_type_title)
    return ReadCargoTypeResponse.model_validate(cargo_type)


# @cargo_types_router.put("/{cargo_type_title}", dependencies=protected_route_deps)
async def update(
    cargo_type_title: str, data: CreateCargoTypeRequest
) -> ReadCargoTypeResponse:
    await CargoTypes.filter(title=cargo_type_title).update(**data.model_dump())
    cargo_type = await CargoTypes.get(title=cargo_type_title)
    return ReadCargoTypeResponse.model_validate(cargo_type)


@cargo_types_router.delete("/{cargo_type_title}", dependencies=protected_route_deps)
async def delete(cargo_type_title: str) -> Status:
    deleted_count = await CargoTypes.filter(title=cargo_type_title).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"CargoType {cargo_type_title} not found"
        )
    return Status(message=f"Deleted CargoType {cargo_type_title}")
