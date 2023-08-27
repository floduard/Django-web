from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import view_registered_users

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('search/flights/', views.search_flights, name='search_flights'),
    path('book_flight/', views.book_flight, name='book_flight'),
    path('search/hotels/', views.search_available_hotels, name='search_hotel'),
    path('search/rental_cars/',views.search_available_rental_cars, name='search_rental_car'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('add/hotel/', views.add_hotel, name='add_hotel'),
    path('add/rental_car/', views.add_rental_car, name='add_rental_car'),
    path('user/view/registered-users/', view_registered_users, name='view_registered_users'),
]
