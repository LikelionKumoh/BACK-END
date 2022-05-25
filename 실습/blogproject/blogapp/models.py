from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)# 어떤 게시물에 달려있는 댓글인지를 알 수 있는, 댓글이 달린 그 게시물이 쓰임

    def __str__(self):
        return self.comment