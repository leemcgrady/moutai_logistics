# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_auto_20181107_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settlement',
            name='number',
            field=models.IntegerField(verbose_name='车牌编号'),
        ),
    ]
