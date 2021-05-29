from rest_framework import serializers
from .models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['from_location'] = {
            "city": instance.from_location.display_name, "country": instance.from_location.country.name}
        representation['to_location'] = {
            "city": instance.to_location.display_name, "country": instance.to_location.country.name}
        return representation

    def validate(self, attrs):
        departure_time = attrs.get('departure_time')
        arrival_time = attrs.get('arrival_time')
        from_location = attrs.get('from_location')
        to_location = attrs.get('to_location')

        if departure_time >= arrival_time:
            raise serializers.ValidationError(
                {"time": "The time of departure cannot be earlier than the time of arrival"})
        elif from_location == to_location:
            raise serializers.ValidationError(
                {"location": "The flight cannot be to the same locations"})

        return attrs
