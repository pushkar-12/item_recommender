# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0004_snap'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='')),
                ('idd', models.IntegerField()),
            ],
        ),
    ]
