from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    name = models.CharField(max_length=20, default='username')
    age = models.IntegerField(default=0)