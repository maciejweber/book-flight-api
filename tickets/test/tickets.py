from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from tickets.models.ticket import Ticket
from flights.choices import TicketsType
from flights.models import Flight
from countries.models import Country
from cities.models import City

from django.template.defaultfilters import slugify


class TicketsTestCase(TestCase):
    ticket_create_url = reverse('tickets:ticket-create')

    FIRST_CLASS_TICKET = {"type": TicketsType.FIRST_CLASS}
    SECOND_CLASS_TICKET = {"type": TicketsType.SECOND_CLASS}

    def login(self):
        self.client.login(username='maciej', password='Password123$')

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(
            username='maciej', email='maciej@o2.pl', password='Password123$')
        self.login()
        country = Country.objects.create(
            name="france", display_name="France")
        first_city = City.objects.create(
            display_name="Paris", country=country)
        second_city = City.objects.create(
            display_name="Lyon", country=country)
        departure_time = timezone.now() + timedelta(days=1)
        arrival_time = timezone.now() + timedelta(days=1) + timedelta(hours=2)
        FLIGHT_DATA = {
            "tickets_type": [
                "first"
            ],
            "departure_time": "2021-06-04T22:07:36Z",
            "arrival_time": "2021-06-04T22:07:37Z",
            "from_location": first_city,
            "to_location": second_city,
            "available_first_class_ticket_quantity": 5,
            "available_second_class_ticket_quantity": 5
        }
        self.flight = Flight.objects.create(**FLIGHT_DATA)

    def test_create_ticket_incorrect_type(self):
        self.SECOND_CLASS_TICKET['user'] = self.user.id
        self.SECOND_CLASS_TICKET['flight'] = self.flight.id
        response = self.client.post(
            self.ticket_create_url, self.SECOND_CLASS_TICKET)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_ticket_correct_type(self):
        self.FIRST_CLASS_TICKET['user'] = self.user.id
        self.FIRST_CLASS_TICKET['flight'] = self.flight.id
        response = self.client.post(
            self.ticket_create_url, self.FIRST_CLASS_TICKET)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
