import json
from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import Country


class BaseTestCase(APITestCase):
    def setUp(self):
        self.username = "Maciej"
        self.password = "Password123@"
        self.user = User.objects.create_superuser(
            username=self.username, email=self.username, password=self.password)
        self.login()

    def login(self):
        self.client.login(username=self.username, password=self.password)

    def tearDown(self):
        Country.objects.all().delete()


class EventAPITestCase(BaseTestCase):
    """
    Test creating and showing correct countries
    """

    country_create_url = reverse("countries:country-create")
    countries_list_url = reverse("countries:country-list")

    COUNTRY_DATA = {
        "name": "france",
        "display_name": "France"
    }

    def test_unauthorized_create_country(self):
        """
        Create country from anonymous user
        """
        self.client.logout()
        response = self.client.post(
            self.country_create_url, self.COUNTRY_DATA)
        self.login()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_create_country(self):
        """
        Create country from authorized user
        """
        self.login()
        response = self.client.post(
            self.country_create_url, self.COUNTRY_DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_countries(self):
        """
        Test get all countries
        """
        self.client.logout()
        self.test_unauthorized_create_country()
        self.test_authorized_create_country()
        response = self.client.get(self.countries_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
