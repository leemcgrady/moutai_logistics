# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0010_auto_20181108_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settlement',
            old_name='number',
            new_name='car_number',
        ),
    ]
