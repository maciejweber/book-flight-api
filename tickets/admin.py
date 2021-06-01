from django.contrib import admin
from .models import Ticket, Discount, Service

admin.site.register(Ticket)
admin.site.register(Discount)
admin.site.register(Service)
