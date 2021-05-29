from django.db import models
from django.db.models.deletion import DO_NOTHING
from countries.models import Country


class City(models.Model):
    name = models.CharField(verbose_name="City name",
                            max_length=30, unique=True)
    display_name = models.CharField(
        "Display name", max_length=30, help_text="Display name should stary with a capital letter", unique=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return "{} ({})".format(self.display_name, self.country)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
