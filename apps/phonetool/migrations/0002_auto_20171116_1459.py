# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonetool', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=5),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
