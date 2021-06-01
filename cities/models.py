from django.db import models
from django.db.models.deletion import DO_NOTHING
from countries.models import Country


class City(models.Model):
    display_name = models.CharField(
        "City name", max_length=30, help_text="Display name should stary with a capital letter", unique=True)
    name = models.CharField(verbose_name="Name",
                            max_length=30, blank=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return "{} ({})".format(self.display_name, self.country)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def save(self, *args, **kwargs):
        self.name = self.display_name.lower()
        super().save(*args, **kwargs)
