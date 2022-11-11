from django.urls import path
from .views import userApi, locationApi, sportApi, get_info_user, login_, locations

urlpatterns = [
    path('user/', userApi),
    path('user/<int:id>', userApi),
    path('locations/', locations),
    path('location/<int:id>', locationApi),
    path('location/', locationApi),
    path('sport/', sportApi),
    path('sport/<int:id>', sportApi),
    path("login/", login_, name="login"),
    path("user_info/", get_info_user),
]