from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import login_, logout_
from django.views.generic import TemplateView
from .views import userApi, locationApi, sportApi
from django.contrib.auth import views as auth_views
# router = routers.DefaultRouter()
# router.register('users', UserViewSet)

urlpatterns = [
    path('user/', userApi),
    path('user/<int:id>', userApi),
    path('location/', locationApi),
    path('location/<int:id>', locationApi),
    path('sport/', sportApi),
    path('sport/<int:id>', sportApi),
    path("login/", login_(), name="login",),
    path("logout/", logout_(), name="logout",),
]
