from rest_framework import permissions, generics, status
from rest_framework.response import Response

from tickets.serializers.payment import PaymentSerializer


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
