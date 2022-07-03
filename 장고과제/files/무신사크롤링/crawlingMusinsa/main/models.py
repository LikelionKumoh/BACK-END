from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Item(models.Model):
    image=models.ImageField()
    brand=models.URLField()
    items=models.URLField()
    rank=models.CharField(max_length=10)
    price=models.CharField(max_length=10)
    likes=models.CharField(max_length=10)
