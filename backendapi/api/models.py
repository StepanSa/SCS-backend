from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    birthDate = models.DateField(blank=True, null=True)


class Sport(models.Model):
    sportId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class Location(models.Model):
    locationId = models.AutoField(primary_key=True)
    sportId = models.ForeignKey('Sport', to_field='sportId', on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    tgChannel = models.CharField(max_length=50)

