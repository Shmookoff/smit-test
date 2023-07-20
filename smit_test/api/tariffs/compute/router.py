from fastapi import APIRouter, Depends, HTTPException, status

from smit_test.api.tariffs.models import Tariffs

from .schemas import ComputeRequestQuery, ComputeResponse

compute_router = APIRouter(prefix="/compute")


@compute_router.get("")
async def compute(query: ComputeRequestQuery = Depends()) -> ComputeResponse:
    tariff = await Tariffs.get_or_none(date=query.date, cargo_type_id=query.cargo_type)
    if not tariff:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Tariff for requested date and cargo_type does not exist.",
        )
    return ComputeResponse(delivery_cost=query.declared_value * tariff.rate)
