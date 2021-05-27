from django.db.models import query
from django.shortcuts import render
from rest_framework import permissions, generics

from .models import Flight
from .serializers import FlightSerializer


class FlightList(generics.ListAPIView):
    """
    Display all active flights
    """

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
