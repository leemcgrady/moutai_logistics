from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
# Create your models here.
import django.utils.timezone as timezone


class Car(BaseModel):
    '''车辆模型类'''
    car_name = models.CharField(max_length=20, verbose_name='车牌号')
    owner_name = models.CharField(max_length=20, null=True, verbose_name='车主姓名')
    owner_phone = models.CharField(max_length=11, null=True, verbose_name='车主电话')
    driver_name = models.CharField(max_length=20, null=True, verbose_name='驾驶员姓名')
    driver_phone = models.CharField(max_length=11, null=True, verbose_name='驾驶员电话')

    class Meta:
        db_table = 'ml_car'
        verbose_name = '车辆'
        verbose_name_plural = verbose_name


class CarTransportLedger(BaseModel):
    '''运输台账模型类'''
    status_choices = (
        (0, '施封'),
        (1, '解封'),
    )
    car = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='操作车辆')
    state = models.SmallIntegerField(default=0, choices=status_choices, verbose_name='施解封状态')
    location = models.CharField(max_length=11, null=True, verbose_name='地点')
    operation_time = models.DateTimeField(default=timezone.now,verbose_name='操作时间')
    problem_registration = models.CharField(max_length=256, verbose_name='问题登记')

    class Meta:
        db_table = 'ml_car_transport_ledger'
        verbose_name = '运输台账'
        verbose_name_plural = verbose_name