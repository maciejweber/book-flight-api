from django.db import models

from .choices import TicketsType
from cities.models import City
from .manager import FlightQuerySet


class Flight(models.Model):
    from_location = models.ForeignKey(
        City, on_delete=models.DO_NOTHING, verbose_name='From location', related_name="from_location")
    to_location = models.ForeignKey(
        City, on_delete=models.DO_NOTHING, verbose_name='To location', related_name="to_location")

    departure_time = models.DateTimeField(verbose_name='Departure time')
    arrival_time = models.DateTimeField(verbose_name='Arrival time')

    tickets_type = models.CharField(max_length=30, choices=TicketsType.CHOICES)

    first_class_ticket_quantity = models.PositiveIntegerField(
        verbose_name='First class ticket quantity', default=0)
    first_class_ticket_price = models.PositiveSmallIntegerField(
        verbose_name='First class ticket price', default=0)

    is_active = models.BooleanField(
        verbose_name="Flight is active", default=False)

    objects = FlightQuerySet.as_manager()

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = "Flights"

    def __str__(self) -> str:
        return "Flight from {} to {}".format(self.from_location, self.to_location)
