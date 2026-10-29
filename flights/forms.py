from django import forms
from .models import Airport, Flight, Passenger


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ["code", "city"]


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ["origin", "destination", "duration"]


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["name", "flights"]
