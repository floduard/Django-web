from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Flight, Hotel, RentalCar
from .forms import FlightBookingForm, HotelSearchForm, RentalCarSearchForm, HotelForm, RentalCarForm

from django.contrib.auth import logout as auth_logout

from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page or any other desired page
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home')


def home(request):
    if request.user.is_authenticated:
        flight_form = FlightBookingForm()

        flights = Flight.objects.all()  # You can modify this query to filter booked flights
        return render(request, 'home_authenticated.html',
                      {'flight_form': flight_form, 'flights': flights})
    else:
        flights = Flight.objects.filter(user=request.user) if request.user.is_authenticated else []

        return render(request, 'bookings/home.html', {'flights': flights})


# In bookings/views.py

def book_flight(request):
    if request.method == 'POST':
        form = FlightBookingForm(request.POST)
        if form.is_valid():
            # Save the form data to the Flight model
            flight = form.save()
            # Redirect or show a success message

    else:
        form = FlightBookingForm()

    context = {'form': form}
    return render(request, 'book_flight.html', context)


def search_flights(request):
    if request.method == 'GET':
        departure_city = request.GET.get('departure_city')
        arrival_city = request.GET.get('arrival_city')

        if departure_city and arrival_city:
            flights = Flight.objects.filter(departure_city__icontains=departure_city)
        else:
            flights = []

        return render(request, 'search_flights.html', {'flights': flights})

    return render(request, 'search_flights.html')


def search_available_hotels(request):
    name = request.GET.get('name')

    if name:
        hotels = Hotel.objects.filter(name__icontains=name)
    else:
        hotels = []

    context = {'hotels': hotels}
    return render(request, 'search_hotels.html', context)


def search_available_rental_cars(request):
    search_form = RentalCarSearchForm(request.GET)
    rental_cars = []

    if search_form.is_valid():
        model = search_form.cleaned_data['model']
        rental_cars = RentalCar.objects.filter(name__icontains=model)

    context = {'search_form': search_form, 'rental_cars': rental_cars}
    return render(request, 'search_rental_cars.html', context)


@login_required
def user_dashboard(request):
    user = request.user
    # You can retrieve additional user-specific data if needed
    return render(request, 'user_dashboard.html', {'user': user})


@login_required
def add_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.user = request.user
            hotel.save()
            return redirect('home')
    else:
        form = HotelForm()

    return render(request, 'add_hotel.html', {'form': form})


@login_required
def add_rental_car(request):
    if request.method == 'POST':
        form = RentalCarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('user_dashboard')
    else:
        form = RentalCarForm()

    return render(request, 'add_rental_car.html', {'form': form})


from django.contrib.auth import get_user_model


def view_registered_users(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'view_registered_users.html', context)


