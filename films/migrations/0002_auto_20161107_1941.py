# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=40)),
                ('city', models.CharField(blank=True, default='', max_length=40)),
                ('state', models.CharField(blank=True, default='', max_length=2)),
                ('num_screens', models.IntegerField()),
                ('digital', models.BooleanField()),
                ('comment_txt', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ('-id',)},
        ),
    ]
