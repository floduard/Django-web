from django.contrib import admin
from .models import Flight, Hotel, RentalCar

admin.site.register(Flight)
admin.site.register(Hotel)
admin.site.register(RentalCar)
