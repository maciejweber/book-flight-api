from tickets.models.ticket import Ticket
from .exceptions import TokenError, BalanceError


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
