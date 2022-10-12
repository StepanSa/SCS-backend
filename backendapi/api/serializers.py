from rest_framework import serializers
from .models import User, Sport, Location
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    birthDate = serializers.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = User
        fields = ('userId', 'firstName', 'lastName', 'email', 'password', 'birthDate')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('sportId', 'name')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('locationId, sportId', 'address', 'tgChannel')



# from rest_framework import serializers
# from django.contrib.auth.models import User
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True, 'required': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user

