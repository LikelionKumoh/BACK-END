from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Memo(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Memo, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
# class FreeMemo(models.Model):
#     title = models.CharField(max_length=50)
#     body = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     auchor = models.ForeignKey(User, on_delete=models.CASCADE)