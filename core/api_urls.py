from django.urls import path, include

urlpatterns = [
    path('cities/', include('cities.urls')),
    path('countries/', include('countries.urls')),
    path('flights/', include('flights.urls')),
    path('tickets/', include('tickets.urls')),
]
