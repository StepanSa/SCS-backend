from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from .models import Sport, Location
from .serializers import SportSerializer, LocationSerializer
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer

import requests
@csrf_exempt
def login_(request):
    if request.method == 'POST':
        body = JSONParser().parse(request)

        username = body['username']
        password1 = body['password']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            return HttpResponse({'GGWP'})
        else:
            # messages.error(request, "Bad Credentials!!")
            return HttpResponse({'badbadbadboy'})


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
            response = JsonResponse("Added successfully", safe=False)
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response
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
def locations(request):
    if request.method == 'GET':
        locations_ = Location.objects.all()
        locations_serializer = LocationSerializer(locations_, many=True)
        return JsonResponse(locations_serializer.data, safe=False)


@csrf_exempt
def locationApi(request, id=None):
    if request.method == 'GET':
        location = Location.objects.get(id=id)
        location_serializer = LocationSerializer(location)

        port = request.get_port()

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        photolink = 'http://' + ip + ':' + port + '/static/stepan.jpg'

        response = dict(location_serializer.data)
        response.update({'photoUrl': photolink})

        return JsonResponse(response, safe=False)
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
        location = Location.objects.get(id=id)
        location.delete()
        return JsonResponse("Deleted successfully", safe=False)
