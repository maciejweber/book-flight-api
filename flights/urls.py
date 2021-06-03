from django.urls import path

from .views import FlightList, FlightCreate, FlightRetrieve

app_name = "flights"

urlpatterns = [
    path('', FlightList.as_view(), name="flights-list"),
    path('create/', FlightCreate.as_view(), name="flight-create"),
    path('detail/<int:pk>/', FlightRetrieve.as_view(), name="flight-detail"),
]
