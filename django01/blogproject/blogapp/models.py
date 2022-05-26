from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    reg_date = models.DateTimeField(auto_now_add=True)
    # 블로그 객체 참조(외래키)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
