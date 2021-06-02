from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.core.mail import send_mail

from tickets.models.ticket import Ticket


@shared_task
def run_disable_reservation_task(ticket_id: int) -> None:
    instance: Ticket = Ticket.objects.get(id=ticket_id)
    if instance and not instance.is_paid:
        # Return one ticket to available tickets
        ticket_type_quantity = getattr(
            instance.flight, "available_{}_class_ticket_quantity".format(instance.type))
        setattr(instance.flight, "available_{}_class_ticket_quantity".format(
            instance.type), ticket_type_quantity + 1)
        instance.flight.save()
        # Delete unpaid ticket
        instance.delete()
