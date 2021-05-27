from django.db import models


class FlightQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)
