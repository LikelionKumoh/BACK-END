from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title