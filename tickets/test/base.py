# from datetime import timedelta
# from django.utils import timezone
# from django.contrib.auth.models import User
# from rest_framework.test import APITestCase

# from tickets.models.ticket import Ticket
# from flights.choices import TicketsType
# from flights.models import Flight
# from countries.models import Country
# from cities.models import City


# class BaseTestCase(APITestCase):
#     departure_time = timezone.now() + timedelta(days=1)
#     arrival_time = timezone.now() + timedelta(days=1) + timedelta(hours=2)

#     COUNTRY_DATA = {
#         "name": "france",
#         "display_name": "France"
#     }

#     FIRST_CITY_DATA = {
#         "display_name": "Paris"
#     }

#     SECOND_CITY_DATA = {
#         "display_name": "Lyon"
#     }

#     FLIGHT_DATA = {
#         "tickets_type": [TicketsType.FIRST_CLASS, TicketsType.SECOND_CLASS],
#         "departure_time": departure_time,
#         "arrival_time": arrival_time,
#         "is_active": True,
#         "available_first_class_ticket_quantity": 5
#     }

#     FIRST_CLASS_TICKET = {"type": TicketsType.FIRST_CLASS}
#     SECOND_CLASS_TICKET = {"type": TicketsType.SECOND_CLASS}

#     def setUp(self):
#         self.username = "Maciej"
#         self.password = "Password123@"
#         self.user = User.objects.create_superuser(
#             username=self.username, email=self.username, password=self.password)
#         self.login()
#         self.createFlight()

#     def createFlight(self):
#         self.country = Country.objects.create(**self.COUNTRY_DATA)
#         cities = ['first_city', 'second_city']
#         cities_data = ['FIRST_CITY_DATA', 'SECOND_CITY_DATA']
#         for index, city in enumerate(cities):
#             value = getattr(self, cities_data[index])
#             value['country'] = self.country
#             setattr(self, city, City.objects.create(**value))

#         self.FLIGHT_DATA['from_location'] = self.first_city
#         self.FLIGHT_DATA['to_location'] = self.second_city
#         self.flight = Flight.objects.create(**self.FLIGHT_DATA)

#     def login(self):
#         self.client.login(username=self.username, password=self.password)

#     def tearDown(self):
#         Ticket.objects.all().delete()
