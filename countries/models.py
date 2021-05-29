from django.db import models


class Country(models.Model):
    name = models.CharField("Country name", max_length=30)
    display_name = models.CharField(
        "Display name", max_length=30, help_text="Display name should stary with a capital letter")

    def __str__(self) -> str:
        return self.display_name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
