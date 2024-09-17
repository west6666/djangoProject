"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# BookingView, TestimonialView, TeamView, ErrorView, ContactView

from django.urls import path
from app.views import IndexView, AboutView, ServiceView, FeatureView, TeamView, TestimonialView, PageView, AppointmentView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServiceView.as_view(), name='service'),
    path('feature/', FeatureView.as_view(), name='feature'),













    path('appointmentView/', AppointmentView.as_view(), name='appointment'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('team/', TeamView.as_view(), name='team'),
    path('404/', PageView.as_view(), name='404'),
    path('contact/', ContactView.as_view(), name='contact'),
]