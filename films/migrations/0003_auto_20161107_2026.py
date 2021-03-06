# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20161107_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=20)),
            ],
            options={
                'ordering': ('description',),
            },
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='theater',
            options={'ordering': ('id',)},
        ),
    ]
