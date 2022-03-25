from django.core.validators import MinValueValidator
from django.db import models


class SteelStructureFabric(models.Model):
    name = models.CharField(max_length=64)


class TransportStatus(models.TextChoices):
    ANNOUNCED = 'UN', 'Выгрузился'
    ONGOING = 'RE', 'Возврат'


class TransportDelivery(models.Model):
    fabric = models.ForeignKey(SteelStructureFabric, on_delete=models.CASCADE)
    date = models.DateField()
    unloading_date = models.DateField()

    doc_id = models.CharField(max_length=64, null=True)
    weight = models.FloatField(validators=[MinValueValidator(0)], null=True)
    status = models.CharField(
        max_length=2,
        choices=TransportStatus.choices,
        null=True,
    )


class DeliveryObject(models.Model):
    delivery = models.ForeignKey(TransportDelivery, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    value = models.FloatField(null=True)
