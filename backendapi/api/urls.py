from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
# from .views import UserViewSet

from .views import userApi, locationApi, sportApi

# router = routers.DefaultRouter()
# router.register('users', UserViewSet)

urlpatterns = [
    path('user/', userApi),
    path('user/<int:id>', userApi),
    path('location/', locationApi),
    path('location/<int:id>', locationApi),
    path('sport/', sportApi),
    path('sport/<int:id>', sportApi),
]
