from flights.models import Flight
from rest_framework import serializers

from .models import Ticket
from flights.serializers import FlightSerializer


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['flight'] = FlightSerializer(
            instance=instance.flight).data
        return representation
