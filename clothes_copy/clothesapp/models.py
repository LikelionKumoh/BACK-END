import email
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    rank = models.CharField(max_length=10)
    img = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)