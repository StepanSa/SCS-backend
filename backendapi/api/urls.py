from django.urls import path
from .views import login_, logout_
from .views import userApi, locationApi, sportApi

urlpatterns = [
    path('user/', userApi),
    path('user/<int:id>', userApi),
    path('location/', locationApi),
    path('location/<int:id>', locationApi),
    path('sport/', sportApi),
    path('sport/<int:id>', sportApi),
    path("login/", login_()),
    path("logout/", logout_()),
]
