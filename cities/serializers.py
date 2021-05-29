from rest_framework import serializers
from .models import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'display_name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['country'] = instance.country.name
        return representation
