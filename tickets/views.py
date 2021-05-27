from django.shortcuts import render
from rest_framework import permissions, generics, serializers
import django_filters.rest_framework

from .models import Ticket
from .serializers import TicketSerializer


class TicketList(generics.ListAPIView):
    """
    Display all tickets
    """

    serializer_class = TicketSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['is_paid', 'type']

    def get_queryset(self):
        return self.request.user.tickets.all()


class TicketCreate(generics.CreateAPIView):
    """
    Create ticket
    """

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAdminUser]
