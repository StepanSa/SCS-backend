from django.db import models


# class User(models.Model):
#     firstName = models.CharField(max_length=30)
#     lastName = models.CharField(max_length=30)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=30)
#     birthDate = models.DateField(blank=True, null=True)


class Location(models.Model):
    sportName = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=150)
    tgChannel = models.URLField(max_length=100)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)


