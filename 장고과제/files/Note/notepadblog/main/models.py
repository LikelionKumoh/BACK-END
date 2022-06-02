from datetime import date
from turtle import title
from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

class Notepad(models.Model):
    # title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body