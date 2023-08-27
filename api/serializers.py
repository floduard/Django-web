from rest_framework import serializers
from bookings.models import Flight, Hotel, RentalCar


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RentalCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalCar
        fields = '__all__'
