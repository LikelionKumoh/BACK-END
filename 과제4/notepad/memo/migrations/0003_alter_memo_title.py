# Generated by Django 4.0.4 on 2022-06-01 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0002_alter_memo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='title',
            field=models.CharField(max_length=5),
        ),
    ]
