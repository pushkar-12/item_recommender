# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0008_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='modifiedname',
            field=models.CharField(default='default', max_length=150),
        ),
    ]