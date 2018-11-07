# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-07 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20181107_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settlement',
            name='ETC_cost',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ETC费用'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='buckle_oil',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='扣油'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='demand_for_cost',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='车主应进费用'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='labor_ticket_amount',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='应开劳务票金额'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='other_cost',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='其他费用'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='taxation_for_bank',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='应交税费（转银行卡）'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='taxation_for_wechat',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='应交税费（转微信）'),
        ),
    ]
