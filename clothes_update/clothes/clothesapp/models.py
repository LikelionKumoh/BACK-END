from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    rank = models.CharField(max_length=10)
    img = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

class MyUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=300)
    email = models.CharField(max_length=200,unique=True)