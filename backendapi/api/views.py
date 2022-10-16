from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import User, Sport, Location
from .serializers import UserSerializer, SportSerializer, LocationSerializer
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse


def login_(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Logged in Successfully!!")
        return redirect(request, 'home.html')
    else:
        return HttpResponse('Bad Credentials')


def logout_(request):
    logout(request)
    messages.success(request, "Logged out Successfully!!")
    return redirect('home')


@csrf_exempt
def userApi(request, id=None):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(userId=user_data['userId'])
        users_serializer = UserSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        user = User.objects.get(userId=id)
        user.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def sportApi(request, id=None):
    if request.method == 'GET':
        sports = Sport.objects.all()
        sports_serializer = SportSerializer(sports, many=True)
        return JsonResponse(sports_serializer.data, safe=False)
    elif request.method == 'POST':
        sport_data = JSONParser().parse(request)
        sports_serializer = SportSerializer(data=sport_data)
        if sports_serializer.is_valid():
            sports_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        sport_data = JSONParser().parse(request)
        sport = User.objects.get(userId=sport_data['SportId'])
        sports_serializer = SportSerializer(sport, data=sport_data)
        if sports_serializer.is_valid():
            sports_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        sport = Sport.objects.get(sportId=id)
        sport.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def locationApi(request, id=None):
    if request.method == 'GET':
        locations = Location.objects.all()
        locations_serializer = LocationSerializer(locations, many=True)
        return JsonResponse(locations_serializer.data, safe=False)
    elif request.method == 'POST':
        location_data = JSONParser().parse(request)
        locations_serializer = LocationSerializer(data=location_data)
        if locations_serializer.is_valid():
            locations_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        location_data = JSONParser().parse(request)
        location = Location.objects.get(locationId=location_data['locationId'])
        locations_serializer = LocationSerializer(location, data=location_data)
        if locations_serializer.is_valid():
            locations_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        location = Location.objects.get(locationId=id)
        location.delete()
        return JsonResponse("Deleted successfully", safe=False)


