# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-06 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(choices=[('Gurgaon', 'Gurgaon'), ('Kapriwas', 'Kapriwas'), ('Manesar', 'Manesar')], max_length=20),
        ),
    ]
