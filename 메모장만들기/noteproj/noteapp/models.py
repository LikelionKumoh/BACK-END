from django.db import models
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
