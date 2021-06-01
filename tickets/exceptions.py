from rest_framework.exceptions import APIException


class PaymentException(APIException):
    message = 'payment exception'


class TokenError(PaymentException):
    pass


class BalanceError(PaymentException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
