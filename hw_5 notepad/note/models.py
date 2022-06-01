from django.db import models


class Memo(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:10]
