from django import forms

from bookings.models import Hotel, RentalCar, Flight


class FlightBookingForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = [
            'traveler_name',
            'email',
            'departure_city',
            'arrival_city',
            'departure_time',
            'price',
            'book_hotel',
            'rent_car',
        ]


class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'location', 'description', 'price', 'image']


class RentalCarBookingForm(forms.ModelForm):
    class Meta:
        model = RentalCar
        fields = ['model', 'date_of_renting', 'price', 'image']


class FlightSearchForm(forms.Form):
    departure_city = forms.CharField(max_length=100, label='Departure City')
    arrival_city = forms.CharField(max_length=100, label='Arrival City')
    # Add other flight search fields as needed


class HotelSearchForm(forms.Form):
    name = forms.CharField(max_length=100, label='hotel_name')


class RentalCarSearchForm(forms.Form):
    model = forms.CharField(label='Car Name', max_length=100)


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'location', 'description', 'price']


class RentalCarForm(forms.ModelForm):
    class Meta:
        model = RentalCar
        fields = ['model', 'date_of_renting', 'price']
