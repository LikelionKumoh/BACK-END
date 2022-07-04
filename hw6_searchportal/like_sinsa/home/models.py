from distutils.command.upload import upload
from django.db import models


class Goods(models.Model):
    rank = models.TextField()
    image = models.ImageField(upload_to="")
    brand_name = models.TextField()
    goods_name = models.TextField()
    price = models.TextField()
    recommand_cnt = models.TextField()

    def __str__(self):
        return self.goods_name