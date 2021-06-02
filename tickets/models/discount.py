from django.db import models


class Discount(models.Model):
    name = models.CharField(verbose_name='Discount name', max_length=50)
    discount_percentage = models.IntegerField(
        verbose_name='Discount percentage')

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self) -> str:
        return "{} ({}%)".format(self.name, self.discount_percentage)
