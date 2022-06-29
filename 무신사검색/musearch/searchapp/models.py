from django.db import models

class SearchModel(models.Model):
    InfoId=models.CharField(max_length=50,default='', blank=True, null=True)
    Name=models.CharField(max_length=50,default='', blank=True, null=True)
    Image=models.CharField(max_length=50,default='', blank=True, null=True)
    Brand=models.CharField(max_length=50,default='', blank=True, null=True)
    Price=models.CharField(max_length=50,default='', blank=True, null=True)
    Rank=models.CharField(max_length=50,default='' ,blank=True, null=True)

    def __str__(self):
        return self.Name

