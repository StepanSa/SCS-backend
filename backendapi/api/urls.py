from django.urls import path
from .views import userApi, locationApi, sportApi, get_info_user, login_
from . import views

urlpatterns = [
    path('user/', userApi),
    path('user/<int:id>', userApi),
    path('location/', locationApi),
    path('location/<int:id>', locationApi),
    path('sport/', sportApi),
    path('sport/<int:id>', sportApi),
    path("login/", login_, name="login"),
    path("user_info/", get_info_user),
]
