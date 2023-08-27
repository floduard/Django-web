from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    description = models.TextField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='destinations/', null=True)

    # Add other hotel-related fields
    def __str__(self):
        return f"{self.name}"


class RentalCar(models.Model):
    model = models.CharField(max_length=100)
    date_of_renting = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='destinations/', null=True)

    # Add other rental car-related fields
    def __str__(self):
        return f"{self.model} - {self.price}"


class Flight(models.Model):
    traveler_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    book_hotel = models.ForeignKey(Hotel, null=True, on_delete=models.CASCADE)
    rent_car = models.ForeignKey(RentalCar, null=True, on_delete=models.CASCADE)

    # Add other flight-related field
    def __str__(self):
        return f"{self.traveler_name} - {self.departure_city} - {self.arrival_city} - {self.departure_time} - {self.price} -{self.book_hotel} - {self.rent_car}"
