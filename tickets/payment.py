from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Ticket
from .exceptions import TokenError, BalanceError


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


class PaymentGateway:
    def payment(self, instance, token, amount):
        if not token:
            raise TokenError("Token is incorrect")
        if amount != instance.price:
            raise BalanceError("Price on ticket is different")
        return self.paid_off(instance)

    @staticmethod
    def paid_off(instance: Ticket) -> Ticket:
        instance.paid_off()
        return instance
