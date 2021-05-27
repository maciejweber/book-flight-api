from rest_framework import generics, permissions

from .models import Country
from .serializers import CountrySerializer


class CountryList(generics.ListAPIView):
    """
    Display all countries
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]


class CountryCreate(generics.CreateAPIView):
    """
    Create country
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAdminUser]
