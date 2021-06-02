from django.contrib import admin
from tickets.models.ticket import Ticket
from tickets.models.discount import Discount
from tickets.models.service import Service

admin.site.register(Ticket)
admin.site.register(Discount)
admin.site.register(Service)
