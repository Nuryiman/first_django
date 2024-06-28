from django.db import models


class Pizza(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()


class Drink(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    volume = models.FloatField()
    is_alcohol = models.BooleanField()
    consist = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()


class Sushi(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    consist = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()


class Burger(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    consist = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
