from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.login_, name="login"),
    path("register/", views.register, name="register"),
    path('', views.index, name='index'),
]
