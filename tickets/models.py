from django.db import models
from django.contrib.auth.models import User

from flights.models import Flight
from flights.choices import TicketsType


class Ticket(models.Model):
    flight = models.ForeignKey(
        Flight, on_delete=models.DO_NOTHING, verbose_name="Flight", related_name="tickets")
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="User", related_name="tickets")
    is_paid = models.BooleanField(default=False, verbose_name="Is paid")
    type = models.CharField(max_length=30, choices=TicketsType.CHOICES,
                            verbose_name="Ticket type")
    price = models.PositiveSmallIntegerField(
        default=0, verbose_name="Ticket price")

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self) -> str:
        return self.user.username
