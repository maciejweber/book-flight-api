from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .models import Flight

__all__ = ("activate_flight_at_task",)


@shared_task
def activate_flight_at_task(flight_id: int) -> None:
    """
    Activate task at the given time
    """
    instance: Flight = Flight.objects.get(id=flight_id)
    if instance and instance.activate_at:
        instance.is_active = True
        instance.save()
