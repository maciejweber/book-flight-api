from rest_framework import serializers
from .models import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'name', 'display_name', 'country']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['country'] = instance.country.display_name
        return representation
