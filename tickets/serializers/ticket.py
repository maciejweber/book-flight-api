from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta

from tickets.models.ticket import Ticket
from tickets.tasks import run_disable_reservation_task
from flights.serializers import FlightSerializer


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['flight'] = FlightSerializer(
            instance=instance.flight).data
        return representation

    def validate(self, attrs):
        type = attrs.get('type')
        flight = attrs.get('flight')
        attrs["price"] = getattr(flight, "{}_class_ticket_price".format(type))
        ticket_type_quantity = getattr(
            flight, "available_{}_class_ticket_quantity".format(type))

        if attrs.get('type') not in flight.tickets_type:
            raise serializers.ValidationError({"type": "Incorrect type"})
        if ticket_type_quantity == 0:
            raise serializers.ValidationError({"quantity": "Out of tickets"})
        if flight.departure_time < timezone.now():
            raise serializers.ValidationError(
                {"flight": "The flight has already taken off"})
        return attrs

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.calculate_price()

        ticket_type_quantity = getattr(
            instance.flight, "available_{}_class_ticket_quantity".format(instance.type))
        # Remove one ticket from available tickets
        setattr(instance.flight, "available_{}_class_ticket_quantity".format(
            instance.type), ticket_type_quantity - 1)

        instance.save()
        instance.flight.save()

        execute_at = timezone.now() + timedelta(seconds=5)
        run_disable_reservation_task.apply_async(
            args=[instance.id], eta=execute_at)
        return instance
