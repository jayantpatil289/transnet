# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-21 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('power', '0004_line_station'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='line',
            table='power_line',
        ),
        migrations.AlterModelTable(
            name='station',
            table='power_station',
        ),
    ]
