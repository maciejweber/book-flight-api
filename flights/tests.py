from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


from rest_framework import status
from rest_framework.test import APITestCase

from flights.models import Flight
from countries.models import Country
from cities.models import City


class BaseTestCase(APITestCase):
    departure_time = timezone.now() + timedelta(days=1)
    arrival_time = timezone.now() + timedelta(days=1) + timedelta(hours=2)

    COUNTRY_DATA = {
        "name": "france",
        "display_name": "France"
    }

    FIRST_CITY_DATA = {
        "display_name": "Paris"
    }
    SECOND_CITY_DATA = {
        "display_name": "Lyon"
    }

    FLIGHT_DATA = {
        "tickets_type": ["first"],
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "is_active": True,

        "first_class_ticket_quantity": 5,
        "available_first_class_ticket_quantity": 5,
        "first_class_ticket_price": "70.00",

        "second_class_ticket_quantity": 0,
        "available_second_class_ticket_quantity": 2,
        "second_class_ticket_price": "0.00",
    }

    def _createCities(self):
        self.country = Country.objects.create(**self.COUNTRY_DATA)
        cities = ['first_city', 'second_city']
        cities_data = ['FIRST_CITY_DATA', 'SECOND_CITY_DATA']
        for index, city in enumerate(cities):
            value = getattr(self, cities_data[index])
            value['country'] = self.country
            setattr(self, city, City.objects.create(**value))

    def setUp(self):
        self.staff_username = "Maciej"
        self.client_username = "Client"
        self.password = "Password123@"
        self.client_user = User.objects.create_user(
            username=self.client_username, email=self.client_username, password=self.password)
        self.staff_user = User.objects.create_superuser(
            username=self.staff_username, email=self.staff_username, password=self.password)
        self._createCities()

    def login_client(self):
        self.client.login(username=self.client_username,
                          password=self.password)

    def login_staff(self):
        self.client.login(
            username=self.staff_username, password=self.password)

    def tearDown(self):
        Flight.objects.all().delete()
        Country.objects.all().delete()
        City.objects.all().delete()


class FlightAPITestCase(BaseTestCase):
    flight_create_url = reverse("flights:flight-create")
    flight_list_url = reverse("flights:flights-list")
    flight_detail = "flights:flight-detail"

    def test_unauthorized_create_flight(self):
        """
        Test create flight from unauthorized user 
        """
        self.client.logout()
        self.FLIGHT_DATA['from_location'] = self.first_city.id
        self.FLIGHT_DATA['to_location'] = self.second_city.id
        response = self.client.post(self.flight_create_url, self.FLIGHT_DATA)
        self.login_staff()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unstaff_create_flight(self):
        """
        Test create flight from unstaff user 
        """
        self.login_client()
        self.FLIGHT_DATA['from_location'] = self.first_city.id
        self.FLIGHT_DATA['to_location'] = self.second_city.id
        response = self.client.post(self.flight_create_url, self.FLIGHT_DATA)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_staff_create_flight(self):
        """
        Test create flight from staff user 
        """
        self.login_staff()
        self.FLIGHT_DATA['from_location'] = self.first_city.id
        self.FLIGHT_DATA['to_location'] = self.second_city.id
        response = self.client.post(self.flight_create_url, self.FLIGHT_DATA)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_time_create_flight(self):
        """
        Test create flight from with incorrect time data
        """
        self.login_staff()
        self.FLIGHT_DATA['from_location'] = self.first_city.id
        self.FLIGHT_DATA['to_location'] = self.first_city.id
        self.FLIGHT_DATA['departure_time'] = self.arrival_time
        self.FLIGHT_DATA['arrival_time'] = self.departure_time
        response = self.client.post(self.flight_create_url, self.FLIGHT_DATA)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_location_create_flight(self):
        """
        Test create flight from with incorrect location data
        """
        self.login_staff()
        self.FLIGHT_DATA['from_location'] = self.first_city.id
        self.FLIGHT_DATA['to_location'] = self.first_city.id
        response = self.client.post(self.flight_create_url, self.FLIGHT_DATA)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_active_flights(self):
        """
        Test list flight
        """
        self.test_unauthorized_create_flight()
        self.test_unstaff_create_flight()
        self.test_staff_create_flight()
        response = self.client.get(self.flight_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
