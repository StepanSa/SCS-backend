from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_, name="login_"),
    path('register/', views.register, name="register"),
]
