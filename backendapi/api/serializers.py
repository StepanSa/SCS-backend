from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Location, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'password', 'email', 'first_name',
                  'last_name', 'instagram_link', 'facebook_link',
                  'telegram_link', 'twitter_link')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'sportName', 'address', 'tgChannel')


class LocationSerializerAnonUser(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'sportName', 'address')
