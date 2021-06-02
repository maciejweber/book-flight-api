from django.db import models


class Service(models.Model):
    name = models.CharField(
        verbose_name='Additional service name', max_length=50)
    service_price = models.DecimalField(max_digits=7, decimal_places=2,
                                        verbose_name='Additional service price')

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.service_price)
