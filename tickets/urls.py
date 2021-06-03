from django.urls import path

from tickets.views.ticket import TicketList, TicketCreate
from tickets.views.payment import PaymentCreate

app_name = 'tickets'

urlpatterns = [
    path('', TicketList.as_view(), name='tickets-list'),
    path('create/', TicketCreate.as_view(), name='ticket-create'),
    path('payment/create/', PaymentCreate.as_view(), name='payment-create')
]
