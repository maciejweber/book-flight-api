import json
from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import City
from countries.models import Country


class BaseTestCase(APITestCase):
    COUNTRY_DATA = {
        "id": 1,
        "name": "poland",
        "display_name": "Poland"
    }

    def setUp(self):
        self.username = "Maciej"
        self.password = "Password123@"
        self.user = User.objects.create_superuser(
            username=self.username, email=self.username, password=self.password)
        self.login()
        self.country = Country.objects.create(**self.COUNTRY_DATA)

    def login(self):
        self.client.login(username=self.username, password=self.password)

    def tearDown(self):
        City.objects.all().delete()


class EventAPITestCase(BaseTestCase):
    """
    Test creating and showing correct cities
    """

    city_create_url = reverse("cities:city-create")
    cities_list_url = reverse("cities:cities-list")

    city_DATA = {
        "name": "warsaw",
        "display_name": "Warsaw"
    }

    def test_unauthorized_create_city(self):
        """
        Create city from anonymous user
        """
        self.client.logout()
        self.city_DATA['country'] = self.country.id
        response = self.client.post(
            self.city_create_url, self.city_DATA)
        self.login()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_create_city(self):
        """
        Create city from authorized user
        """
        self.login()
        self.city_DATA['country'] = 1
        response = self.client.post(
            self.city_create_url, self.city_DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_cities(self):
        """
        Test get all cities
        """
        self.client.logout()
        self.test_unauthorized_create_city()
        self.test_authorized_create_city()
        response = self.client.get(self.cities_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
