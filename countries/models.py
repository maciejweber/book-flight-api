from django.db import models


class Country(models.Model):
    display_name = models.CharField(
        "City name", max_length=30, help_text="Display name should stary with a capital letter")
    name = models.CharField(verbose_name="Name",
                            max_length=30, blank=True)

    def __str__(self) -> str:
        return self.display_name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def save(self, *args, **kwargs):
        self.name = self.display_name.lower()
        super().save(*args, **kwargs)
