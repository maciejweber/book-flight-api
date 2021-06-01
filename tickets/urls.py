from django.urls import path

from .views import TicketList, TicketCreate, PaymentCreate

urlpatterns = [
    path('', TicketList.as_view(), name='tickets-list'),
    path('create/', TicketCreate.as_view(), name='ticket-create'),
    path('payment/create/', PaymentCreate.as_view(), name='payment-create')
]
