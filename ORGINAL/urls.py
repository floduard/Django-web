"""
URL configuration for ORGINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import PasswordResetView, PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),
    path('api/', include('api.urls')),
    path('docs/', TemplateView.as_view(template_name='_build/index.html'), name='documentation'),
    path('accounts/', include('allauth.urls')),
    path('password/reset/', PasswordResetView.as_view(), name='account_reset_password'),

    # Password change URL
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
