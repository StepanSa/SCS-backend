from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import JSONParser
from .models import Location
from .serializers import LocationSerializer, LocationSerializerAnonUser
from .serializers import UserSerializer
from .uitls import keys_in
from .functions import haversine


def get_info_user(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return JsonResponse("You are not authenticated", safe=False, status=400)
        print(request.user.username)
        print(request.user.email)
        return JsonResponse({
            "username": request.user.username,
            "email": request.user.email
        }, safe=False, status=200)

@csrf_exempt
def login_(request):
    print('inside login')
    if request.method == 'POST':
        print('inside post')
        if request.user.is_authenticated:
            return JsonResponse("You are already authenticated", safe=False, status=200)
        print(request.user)

        body = JSONParser().parse(request)

        username = body['username']
        password = body['password']

        users = User.objects.filter(username=username)

        if len(users) == 0:
            return JsonResponse("User with such username doen't exist", safe=False, status=400)

        user = authenticate(username=username, password=password)

        if user is not None:
            print("in if")
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            res = JsonResponse("User is logged in", safe=False, status=200)
            res['Access-Control-Allow-Credentials'] = 'true'
            # res['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3006'
            res['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,UPDATE,OPTIONS'
            res['Access-Control-Allow-Headers'] = 'X-Requested-With, X-HTTP-Method-Override, Content-Type, Accept'
            return res
        else:
            # messages.error(request, "Bad Credentials!!")
            return JsonResponse("Wrong password", safe=False, status=400)
    elif request.method == 'OPTIONS':
        print('options')


@csrf_exempt
def userApi(request, id=None):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        body = JSONParser().parse(request)

        # Check if all the data are passed
        if not keys_in(body, ['username', 'email', 'first_name', 'last_name', 'password']):
            return JsonResponse("You missed some data", safe=False, status=400)

        # Find users with the same username or email
        users = User.objects.filter(Q(username=body['username']) | Q(email=body['email']))

        if len(users) > 0:
            return JsonResponse("User with such username or email already exists", safe=False, status=400)

        # Check if all data have suitable length
        if not (len(body['password']) > 7 and len(body['username']) > 1 and len(body['email']) >= 1 and \
                len(body['first_name']) >= 1 and len(body['last_name']) >= 1):
            return JsonResponse("Please, check length of your data", safe=False, status=400)

        # Validating email
        try:
            validate_email(body['email'])
        except ValidationError as e:
            return JsonResponse("Please, enter valid email", safe=False, status=400)

        user_serializer = UserSerializer(data=body)

        if not user_serializer.is_valid():
            print(user_serializer.error_messages)
            return JsonResponse("Failed to add", safe=False, status=400)

        user_serializer.save()
        return JsonResponse("Added successfully", safe=False, status=201)

    elif request.method == 'PUT':
        body = JSONParser().parse(request)

        # Check if all the data are passed
        if not keys_in(body, ['id']):
            return JsonResponse("You missed id", safe=False, status=400)

        user = User.objects.get(pk=body['id'])
        if user is None:
            return JsonResponse("User with such id doesn't exist", safe=False, status=400)

        # 1. If field's length is not suitable => statys 400, check your field's length
        for field in body.keys():
            if field == 'password' and len(body[field]) <= 7:
                return JsonResponse("Check your field's length", safe=False, status=400)
            elif field == 'username' and len(body[field]) <= 1:
                return JsonResponse("Check your field's length", safe=False, status=400)
            elif field == 'email' and len(body[field]) < 1:
                return JsonResponse("Check your field's length", safe=False, status=400)
            elif field == 'first_name' and len(body[field]) < 1:
                return JsonResponse("Check your field's length", safe=False, status=400)
            elif field == 'last_name' and len(body[field]) < 1:
                return JsonResponse("Check your field's length", safe=False, status=400)

        for field in body.keys():
            if field == 'password':
                setattr(user, field, make_password(body[field]))
            if field in ['username', 'email', 'first_name', 'last_name']:
                setattr(user, field, body[field])

        user.save()
        return JsonResponse("Updated successfully", safe=False, status=200)

    elif request.method == 'DELETE':
        user = User.objects.get(pk=id)
        if user is None:
            return JsonResponse("There is no user with such id", safe=False, status=400)
        user.delete()
        return JsonResponse("Deleted successfully", safe=False, status=200)


@csrf_exempt
def locations(request):
    if request.method == 'GET':
        locations_ = Location.objects.all()
        locations_serializer = LocationSerializer(locations_, many=True)
        return JsonResponse(locations_serializer.data, safe=False)


@csrf_exempt
def locationsInRadius(request, radius=10000):
    if request.method == 'GET':
        data = request.body
        print(data)
        locations = Location.objects.all()
        res_loc = []

        port = request.get_port()

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        for location in locations:
            if haversine(1, 1, location.latitude, location.longitude) <= radius:
                location_serializer = LocationSerializerAnonUser(location)

                photolink = 'http://' + ip + ':' + port + '/static/' + str(location.id) + '.jpg'

                response = dict(location_serializer.data)
                response.update({'photoUrl': photolink})
                res_loc.append(response)
        return JsonResponse(res_loc, safe=False)



@csrf_exempt
def locationApi(request, id=None):
    if request.method == 'GET':
        if request.user.is_authenticated:
            locations = Location.objects.all()
            res_loc = []

            port = request.get_port()

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            for location in locations:
                location_serializer = LocationSerializer(location)

                photolink = 'http://' + ip + ':' + port + '/static/' + str(location.id) + '.jpg'

                response = dict(location_serializer.data)
                response.update({'photoUrl': photolink})
                res_loc.append(response)
            return JsonResponse(res_loc, safe=False)
        locations = Location.objects.all()
        res_loc = []

        port = request.get_port()

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        for location in locations:
            location_serializer = LocationSerializerAnonUser(location)

            photolink = 'http://' + ip + ':' + port + '/static/' + str(location.id) + '.jpg'

            response = dict(location_serializer.data)
            response.update({'photoUrl': photolink})
            res_loc.append(response)
        return JsonResponse(res_loc, safe=False)
    elif request.method == 'POST':
        location_data = JSONParser().parse(request)
        print(location_data)
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
