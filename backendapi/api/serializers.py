from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import User, Sport, Location
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'email', 'password', 'birthDate']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id, sportId', 'address', 'tgChannel']


