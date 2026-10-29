from django.urls import path
from . import views

app_name = "flights"

urlpatterns = [
    path("", views.index, name="index"),
    path("airports/", views.airports, name="airports"),
    path("passengers/", views.passengers, name="passengers"),

    path("airports/create/", views.airport_create, name="airport_create"),
    path("create/", views.flight_create, name="flight_create"),
    path("passengers/create/", views.passenger_create, name="passenger_create"),
]
