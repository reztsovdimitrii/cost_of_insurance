from tortoise import fields
from tortoise.models import Model


class CargoRate(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=255)
    rate = fields.FloatField()
    date = fields.DateField(
        auto_now_add=True,
        format="%Y-%m-%d"
    )

    class Meta:
        table = "cargo_rates"
        unique_together = (("date", "cargo_type"), )
