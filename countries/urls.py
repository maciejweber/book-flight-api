from django.urls import path

from .views import CountryList, CountryCreate

urlpatterns = [
    path('', CountryList.as_view(), name="country-list"),
    path('create/', CountryCreate.as_view(), name="country-create"),
]
