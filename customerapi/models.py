#A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table

from math import fabs
from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class Restaurant(models.Model):
    restaurantId = models.AutoField(primary_key=True)
    restaurantName = models.CharField(max_length=500)
    restaurantAddress = models.CharField(max_length=500)
    userId = models.IntegerField(blank=False)

    def __str__(self):
        return f"Restaurant #{self.restaurantId}"


class Menu(models.Model):
    menutId = models.AutoField(primary_key=True)
    menuName = models.CharField(max_length=500)
    menuDescription = models.CharField(max_length=500)
    restaurantId = models.IntegerField(blank=False)
    menuDate = models.DateField()

    def __str__(self):
        return f"Menu #{self.menutId}"

class Vote(models.Model):
    voteId = models.AutoField(primary_key=True)
    voteMenuId = models.IntegerField(blank=False)
    userId = models.IntegerField(blank=False)
    voteMenuDate = models.DateField()

    def __str__(self):
        return f"Vote #{self.voteId}"



