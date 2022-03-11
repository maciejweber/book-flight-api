from django.db import models
from django.core.validators import MinValueValidator
from multiselectfield import MultiSelectField
from decimal import Decimal
from datetime import timezone

from .choices import TicketsType
from .manager import FlightQuerySet
from cities.models import City


class Flight(models.Model):
    from_location = models.ForeignKey(
        City, on_delete=models.DO_NOTHING, verbose_name='From location', related_name="from_location")
    to_location = models.ForeignKey(
        City, on_delete=models.DO_NOTHING, verbose_name='To location', related_name="to_location")

    departure_time = models.DateTimeField(verbose_name='Departure time')
    arrival_time = models.DateTimeField(verbose_name='Arrival time')

    tickets_type = MultiSelectField(max_length=30, choices=TicketsType.CHOICES)

    first_class_ticket_quantity = models.PositiveIntegerField(
        verbose_name='First class ticket quantity', default=0)
    available_first_class_ticket_quantity = models.PositiveIntegerField(
        verbose_name='Available first class ticket quantity', default=0)
    first_class_ticket_price = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.00'))],
                                                   verbose_name='First class ticket price', default=0)

    second_class_ticket_quantity = models.PositiveIntegerField(
        verbose_name='Second class ticket quantity', default=0)
    available_second_class_ticket_quantity = models.PositiveIntegerField(
        verbose_name='Available second class ticket quantity', default=0)
    second_class_ticket_price = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.00'))],
                                                    verbose_name='Second class ticket price', default=0)

    is_active = models.BooleanField(
        verbose_name="Flight is active", default=False)
    activate_at = models.DateTimeField(
        verbose_name='Activate at', null=True, blank=True)

    objects = FlightQuerySet.as_manager()

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = "Flights"

    def __str__(self) -> str:
        return "Flight from {} to {}".format(self.from_location, self.to_location)

    def save(self, *args, **kwargs):
        if self.available_first_class_ticket_quantity is None:
            self.available_first_class_ticket_quantity = self.first_class_ticket_quantity

        super().save(*args, **kwargs)
