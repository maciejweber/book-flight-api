from django_filters import rest_framework as filters

from .models import Flight


class FlightFilter(filters.FilterSet):
    from_city = filters.CharFilter(
        field_name="from_location", lookup_expr='name')
    from_country = filters.CharFilter(
        field_name="from_location", lookup_expr='country__name')

    to_city = filters.CharFilter(
        field_name="to_location", lookup_expr='name')
    to_country = filters.CharFilter(
        field_name="to_location", lookup_expr='country__name')

    class Meta:
        model = Flight
        fields = ['from_city', 'from_country']
