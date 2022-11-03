from django.urls import path
from .views import userApi, locationApi, sportApi, test_cookie
from . import views

urlpatterns = [
    path('user/', userApi),
    path('user/<int:id>', userApi),
    path('location/', locationApi),
    path('location/<int:id>', locationApi),
    path('sport/', sportApi),
    path('sport/<int:id>', sportApi),
    path('test/', test_cookie),
    path("login/", views.login_, name="login"),
]
