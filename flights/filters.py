from django_filters import rest_framework as filters

from .models import Flight


class FlightFilter(filters.FilterSet):
    from_location = filters.CharFilter(
        field_name="from_location", lookup_expr='name')
    to_location = filters.CharFilter(
        field_name="to_location", lookup_expr='name')

    class Meta:
        model = Flight
        fields = ['from_location', 'to_location']
