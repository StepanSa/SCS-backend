from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import JsonResponse
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def test_endpoint(request):
    return JsonResponse({
        "status": "ok"
    })