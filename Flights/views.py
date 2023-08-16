from django.shortcuts import render
from .models import Airport, Flight, Passenger
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.

def list(request):
    return render(request, "flights/list.html", {"flights": Flight.objects.all()})

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except:
        raise Http404()
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html", {"flight": flight, 
                                                   "passengers":passengers, 
                                                   "non_passengers":Passenger.objects.exclude(flights=flight).all()
                                                   })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=[flight.id]))
