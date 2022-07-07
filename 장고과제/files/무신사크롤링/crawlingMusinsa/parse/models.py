from django.db import models


class Accounts(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'accounts'


class Parsed(models.Model):
    image = models.TextField(blank=True, null=True)
    ranking = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    item = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=30, blank=True, null=True)
    likes = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.item

    class Meta:
        managed = False
        db_table = 'parsed'