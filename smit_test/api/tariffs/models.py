from typing import TYPE_CHECKING

from tortoise import fields, models

if TYPE_CHECKING:
    from smit_test.api.cargo_types import CargoTypes


class Tariffs(models.Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    cargo_type: fields.ForeignKeyRelation["CargoTypes"] = fields.ForeignKeyField(
        "models.CargoTypes", related_name="tariffs"
    )
    rate = fields.FloatField()

    class Meta:
        unique_together = (("date", "cargo_type"),)
