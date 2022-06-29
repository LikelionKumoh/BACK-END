from django.db import models

class Table(models.Model):
    rank = models.TextField()
    img = models.TextField()
    brand = models.TextField()
    item = models.TextField()
    price = models.TextField()

    def __str__(self):
        return self.item
