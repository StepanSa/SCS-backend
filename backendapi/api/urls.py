from django.urls import path
from .views import userApi, locationApi, get_info_user, login_, locations, locationsInRadius

urlpatterns = [
    path('user/', userApi),
    path('user/<int:id>', userApi),
    path('locations/', locations),
    path('location/<int:id>', locationApi),
    path('location/', locationApi),
    path('location_in_radius/', locationsInRadius),
    path("login/", login_, name="login"),
    path("user_info/", get_info_user),
]