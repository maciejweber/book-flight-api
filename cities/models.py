from django.db import models
from django.db.models.deletion import DO_NOTHING
from countries.models import Country


class City(models.Model):
    name = models.CharField("City name", max_length=30)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.country)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
