from django.db import models


class Country(models.Model):
    name = models.CharField("Country name", max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
