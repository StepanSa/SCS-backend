from django.urls import path
from .views import userApi, locationApi, sportApi, locations
from . import views

urlpatterns = [
    path('user/', userApi),
    path('user/<int:id>', userApi),
    path('locations/', locations),
    path('location/<int:id>', locationApi),
    path('location/', locationApi),
    path('sport/', sportApi),
    path('sport/<int:id>', sportApi),
    path("login/", views.login_, name="login"),
]
