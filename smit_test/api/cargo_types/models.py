from tortoise import fields, models

from smit_test.api.tariffs import Tariffs


class CargoTypes(models.Model):
    title = fields.CharField(255, pk=True, generated=False)

    tariffs: fields.ReverseRelation[Tariffs]
