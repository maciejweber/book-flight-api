from rest_framework import permissions, generics
import django_filters.rest_framework

from tickets.models.ticket import Ticket
from tickets.serializers.ticket import TicketSerializer


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
