# Generated by Django 4.0.4 on 2022-05-11 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 2, 33, 34, 499355)),
        ),
    ]
