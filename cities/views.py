from rest_framework import generics, permissions

from .models import City
from .serializers import CitySerializer


class CityList(generics.ListAPIView):
    """
    Display all cities
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]


class CityCreate(generics.CreateAPIView):
    """
    Create city
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAdminUser]
