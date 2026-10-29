from django.shortcuts import render, redirect

from .models import Airport, Flight, Passenger
from .forms import AirportForm, FlightForm, PassengerForm


def index(request):
    flights = (
        Flight.objects
        .select_related("origin", "destination")
        .prefetch_related("passengers")
        .order_by("id")
    )

    return render(
        request,
        "flights/index.html",
        {"flights": flights},
    )


def airports(request):
    airports = Airport.objects.all().order_by("city", "code")

    return render(
        request,
        "flights/airports.html",
        {"airports": airports},
    )


def passengers(request):
    passengers = (
        Passenger.objects
        .prefetch_related("flights__origin", "flights__destination")
        .order_by("name")
    )

    return render(
        request,
        "flights/passengers.html",
        {"passengers": passengers},
    )


def airport_create(request):
    if request.method == "POST":
        form = AirportForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("flights:airports")
    else:
        form = AirportForm()

    return render(
        request,
        "flights/airport_form.html",
        {"form": form},
    )


def flight_create(request):
    if request.method == "POST":
        form = FlightForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("flights:index")
    else:
        form = FlightForm()

    return render(
        request,
        "flights/flight_form.html",
        {"form": form},
    )


def passenger_create(request):
    if request.method == "POST":
        form = PassengerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("flights:passengers")
    else:
        form = PassengerForm()

    return render(
        request,
        "flights/passenger_form.html",
        {"form": form},
    )
