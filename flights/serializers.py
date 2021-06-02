from rest_framework import serializers
from rest_framework import fields
from datetime import timedelta
from django.utils import timezone

from .models import Flight
from .choices import TicketsType
from .tasks import activate_flight_at_task


class FlightSerializer(serializers.ModelSerializer):
    tickets_type = fields.MultipleChoiceField(choices=TicketsType.CHOICES)

    class Meta:
        model = Flight
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['from_location'] = {
            "city": instance.from_location.display_name, "country": instance.from_location.country.display_name}
        representation['to_location'] = {
            "city": instance.to_location.display_name, "country": instance.to_location.country.display_name}
        return representation

    def validate(self, attrs):
        departure_time = attrs.get('departure_time')
        arrival_time = attrs.get('arrival_time')
        from_location = attrs.get('from_location')
        to_location = attrs.get('to_location')

        if departure_time >= arrival_time:
            raise serializers.ValidationError(
                {"time": "The time of departure cannot be earlier than the time of arrival"})
        if from_location == to_location:
            raise serializers.ValidationError(
                {"location": "The flight cannot be to the same locations"})

        return attrs

    def create(self, validated_data):
        instance = super().create(validated_data)
        if instance.activate_at:
            activate_flight_at_task.apply_async(
                args=[instance.id], eta=instance.activate_at)
        return instance
