from django.db import models
from django.contrib.auth.models import User

from flights.models import Flight
from flights.choices import TicketsType
from .managers import TicketQuerySet


class Discount(models.Model):
    name = models.CharField(verbose_name='Discount name', max_length=50)
    discount_percentage = models.IntegerField(
        verbose_name='Discount percentage')

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self) -> str:
        return "{} ({}%)".format(self.name, self.discount_percentage)


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


class Ticket(models.Model):
    flight = models.ForeignKey(
        Flight, on_delete=models.DO_NOTHING, verbose_name="Flight", related_name="tickets")
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="User", related_name="tickets")
    is_paid = models.BooleanField(default=False, verbose_name="Is paid")
    type = models.CharField(max_length=30, choices=TicketsType.CHOICES,
                            verbose_name="Ticket type")
    price = models.DecimalField(max_digits=7, decimal_places=2,
                                default=0, verbose_name="Ticket price")

    discount = models.ForeignKey(
        Discount, on_delete=models.DO_NOTHING, related_name="tickets", blank=True, null=True)

    service = models.ManyToManyField(
        Service, related_name="tickets", blank=True, null=True)

    objects = TicketQuerySet.as_manager()

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self) -> str:
        return self.user.username

    def paid_off(self) -> None:
        self.is_paid = True
        self.save()

    def calculate_price(self) -> None:
        if self.discount:
            self.price = self.price - \
                (self.price / 100) * self.discount.discount_percentage
        if self.service:
            for service in self.service.all():
                self.price += service.service_price
        self.save()
