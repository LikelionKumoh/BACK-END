from operator import mod
from django.db import models

class UserModel(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.username