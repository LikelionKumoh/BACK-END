from django.db import models

class ComLan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'com_lan'
