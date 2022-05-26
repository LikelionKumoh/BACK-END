from django.db import models

class Memo(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True)    
    body = models.TextField()

    def __str__(self):
        return self.body


