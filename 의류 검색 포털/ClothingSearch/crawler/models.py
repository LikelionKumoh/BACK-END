from distutils.command.upload import upload
from django.db import models

class ClothingData(models.Model):
    rank = models.CharField(max_length=30)
    image = models.ImageField(null=True, upload_to='clothing_image')
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    product = models.CharField(max_length=200)
    #like = models.CharField(max_length=50)

    def __str__(self):
        return self.product  