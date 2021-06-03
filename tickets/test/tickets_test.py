from datetime import timedelta

from django.utils import timezone
from django.urls import reverse
from rest_framework import status

from .base import BaseTestCase


class TicketAPITestCase(BaseTestCase):
    ticket_create_url = reverse('tickets:ticket-create')

    # def test_create_ticket_incorrect_type(self):
    #     self.client.login()
    #     self.SECOND_CLASS_TICKET['flight'] = self.flight.id
    #     response = self.client.post(
    #         self.ticket_create_url, self.FIRST_CLASS_TICKET)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_create_ticket_correct_type(self):
    #     self.client.login()
    #     self.SECOND_CLASS_TICKET['user'] = self.user.id
    #     response = self.client.post(
    #         self.ticket_create_url, self.SECOND_CLASS_TICKET)
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
