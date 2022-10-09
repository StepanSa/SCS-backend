# from rest_framework import viewsets
# from django.contrib.auth.models import User

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import User, Sport, Location
from .serializers import UserSerializer, SportSerializer, LocationSerializer




