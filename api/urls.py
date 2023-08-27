from django.urls import path
from rest_framework import routers, permissions

from . import views
from .views import FlightViewSet, HotelViewSet, RentalCarViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'RentalCar', RentalCarViewSet)

urlpatterns = [
    path('api/', views.api_endpoint, name='api_endpoint'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
# ...

urlpatterns += router.urls
