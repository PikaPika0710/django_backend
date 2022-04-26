# Generated by Django 2.2 on 2022-04-25 17:30

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=1000)),
                ('time_create', models.DateTimeField(default=datetime.datetime(2022, 4, 26, 0, 30, 36, 184586))),
            ],
        ),
    ]
