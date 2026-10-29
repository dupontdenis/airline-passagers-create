from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} - {self.city}"


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="departures",
    )
    destination = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name="arrivals",
    )
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin.code} → {self.destination.code}"


class Passenger(models.Model):
    name = models.CharField(max_length=100)
    flights = models.ManyToManyField(
        Flight,
        related_name="passengers",
        blank=True,
    )

    def __str__(self):
        return self.name
