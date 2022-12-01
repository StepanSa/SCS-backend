from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Location


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'sportName', 'address', 'tgChannel')


class LocationSerializerAnonUser(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'sportName', 'address')
