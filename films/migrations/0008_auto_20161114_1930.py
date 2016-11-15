# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_remove_theater_films'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='theaters',
        ),
        migrations.AddField(
            model_name='theater',
            name='films',
            field=models.ManyToManyField(blank=True, to='films.Film'),
        ),
    ]
