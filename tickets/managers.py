from django.db import models


class TicketQuerySet(models.QuerySet):
    def paid(self):
        return self.filter(is_paid=True)

    def unpaid(self):
        return self.filter(is_paid=False)
