from distutils import text_file
from django.db import models

class Member(models.Model):
    username = models.TextField()
    password = models.TextField()
