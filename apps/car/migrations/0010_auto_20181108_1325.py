# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_auto_20181108_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='车牌编号'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='车牌编号'),
        ),
    ]
