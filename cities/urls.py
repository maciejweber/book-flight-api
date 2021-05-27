from django.urls import path

from .views import CityList, CityCreate

urlpatterns = [
    path('', CityList.as_view(), name="cities-list"),
    path('create/', CityCreate.as_view(), name="city-create"),
]
