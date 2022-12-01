from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    instagram_link = models.URLField(max_length=100, null=True)
    facebook_link = models.URLField(max_length=100, null=True)
    telegram_link = models.URLField(max_length=100, null=True)
    twitter_link = models.URLField(max_length=100, null=True)


class Sport(models.Model):
    name = models.CharField(max_length=30)


class Location(models.Model):
    sportName = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=150)
    tgChannel = models.URLField(max_length=100)
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)

