# Generated by Django 2.1.3 on 2018-11-06 13:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('car_name', models.CharField(max_length=20, verbose_name='车牌号')),
                ('owner_name', models.CharField(max_length=20, null=True, verbose_name='车主姓名')),
                ('owner_phone', models.CharField(max_length=11, null=True, verbose_name='车主电话')),
                ('driver_name', models.CharField(max_length=20, null=True, verbose_name='驾驶员姓名')),
                ('driver_phone', models.CharField(max_length=11, null=True, verbose_name='驾驶员电话')),
            ],
            options={
                'verbose_name': '车辆',
                'verbose_name_plural': '车辆',
                'db_table': 'ml_car',
            },
        ),
        migrations.CreateModel(
            name='CarTransportLedger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('state', models.SmallIntegerField(choices=[(0, '施封'), (1, '解封')], default=0, verbose_name='施解封状态')),
                ('location', models.CharField(max_length=11, null=True, verbose_name='地点')),
                ('operation_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='操作时间')),
                ('problem_registration', models.CharField(max_length=256, verbose_name='问题登记')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Car', verbose_name='操作车辆')),
            ],
            options={
                'verbose_name': '运输台账',
                'verbose_name_plural': '运输台账',
                'db_table': 'ml_car_transport_ledger',
            },
        ),
    ]