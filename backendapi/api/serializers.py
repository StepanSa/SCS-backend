from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Sport, Location


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('sportId', 'name')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('locationId', 'sportName', 'address', 'tgChannel')


