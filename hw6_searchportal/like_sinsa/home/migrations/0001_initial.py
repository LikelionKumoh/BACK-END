# Generated by Django 3.1.3 on 2022-07-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('brand_name', models.TextField()),
                ('goods_name', models.TextField()),
                ('price', models.TextField()),
                ('recommand_cnt', models.TextField()),
            ],
        ),
    ]
