# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-21 16:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('power', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LineModel',
            new_name='Line',
        ),
        migrations.RenameModel(
            old_name='StationModel',
            new_name='Station',
        ),
        migrations.RenameField(
            model_name='line',
            old_name='line',
            new_name='line_string',
        ),
    ]
