# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-06 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_auto_20180407_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_services',
            name='date',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='vendor_services',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]