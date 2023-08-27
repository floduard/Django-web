from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets


from bookings.models import Flight, Hotel, RentalCar
from .serializers import FlightSerializer, HotelSerializer, RentalCarSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RentalCarViewSet(viewsets.ModelViewSet):
    queryset = RentalCar.objects.all()
    serializer_class = RentalCarSerializer


def api_endpoint(request):
    api_url = 'http://localhost:8000/api/swagger'  # Replace with your API endpoint URL
    return render(request, 'api_endpoint.html', {'api_url': api_url})


