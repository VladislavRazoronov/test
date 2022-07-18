from django.db import models

# Create your models here.

class Restaurant(models.Model):

    name = models.CharField(max_length=80)

    website = models.URLField()

class Menus(models.Model):

    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    #Field day represents day of the week as an 0-6 integer ie. Monday = 0, Wednesday = 2
    day = models.IntegerField()

    name = models.CharField(max_length=80)

    description = models.CharField(max_length=300)

    content = models.URLField()

class Employee(models.Model):

    name = models.CharField(max_length=80)

    email = models.EmailField()

    #References the menu that the employee voted for Null if employee didn't vote yet
    voted_for = models.ForeignKey(Menus,on_delete=models.SET_NULL, null=True)