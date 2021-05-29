from django.db.models import query
from django.shortcuts import render
from rest_framework import permissions, generics
from django_filters import rest_framework as filters

from .models import Flight
from .serializers import FlightSerializer
from .filters import FlightFilter


class FlightList(generics.ListAPIView):
    """
    Display all active flights
    """
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FlightFilter
    queryset = Flight.objects.active()

    serializer_class = FlightSerializer
    permission_classes = [permissions.AllowAny]


class FlightCreate(generics.CreateAPIView):
    """
    Create flight
    """

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAdminUser]


class FlightRetrieve(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update, delete flight
    """

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAdminUser]
