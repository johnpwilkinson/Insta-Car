# Generated by Django 3.1.2 on 2020-10-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_post', '0002_auto_20201016_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
