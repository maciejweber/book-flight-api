from django.shortcuts import render
from rest_framework import permissions, generics, status
from rest_framework.response import Response
import django_filters.rest_framework

from .models import Ticket
from .serializers import TicketSerializer
from .payment import PaymentSerializer


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
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaymentCreate(generics.GenericAPIView):
    """
    Create payment for ticket
    """
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
