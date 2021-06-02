from rest_framework import serializers

from datetime import timedelta

from tickets.models.ticket import Ticket
from tickets.payment import PaymentGateway


class PaymentSerializer(serializers.Serializer):
    token = serializers.CharField()
    ticket = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.unpaid())
    amount = serializers.IntegerField()

    def validate(self, attrs):
        token = attrs.get('token')
        ticket = attrs.get('ticket')
        amount = attrs.get('amount')

        PaymentGateway().payment(ticket, token, amount)

        return attrs

    def create(self, validated_data):
        instance = super().create(validated_data)

        # SEND MAIL ABOUT SUCCESSFUL TRANSACTION
        # SEND MAIL REMINDING ABOUT FLIGHT THE DAY BEFORE
        day_before_flight = instance.departure_time - timedelta(days=1)

        return instance
