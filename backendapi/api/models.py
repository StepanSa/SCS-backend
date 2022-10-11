from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    birthDate = models.DateField(blank=True, null=True)


class Sport(models.Model):
    sportId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class Location(models.Model):
    locationId = models.AutoField(primary_key=True)
    sportId = models.ForeignKey('Sport', on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    tgChannel = models.CharField(max_length=50)


