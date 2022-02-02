from django.db import models

from FoodingHelper import settings
from Kitchen.views import User


class Ingredients(models.Model):
    product = models.OneToOneField(User, on_delete=models.CASCADE)


class KitchenModels(models.Model):
    name_dishes = models.CharField(max_length=255)
    cooking = models.TextField
    ingredients = models.ForeignKey(Ingredients, unique=False, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)