from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
# Create your models here.
import django.utils.timezone as timezone


class Car(BaseModel):
    '''车辆模型类'''
    car_number = models.IntegerField(blank=True, null=True, verbose_name='车牌编号')
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
    car_id = models.IntegerField(blank=True, null=True, verbose_name='car_id')
    car_name = models.CharField(max_length=20, verbose_name='车牌号')
    state = models.SmallIntegerField(default=0, choices=status_choices, verbose_name='施解封状态')
    location = models.CharField(max_length=11, null=True, verbose_name='地点')
    operation_time = models.DateTimeField(default=timezone.now,verbose_name='操作时间')
    problem_registration = models.CharField(max_length=256, null=True, blank=True, verbose_name='问题登记')

    class Meta:
        db_table = 'ml_car_transport_ledger'
        verbose_name = '运输台账'
        verbose_name_plural = verbose_name


class Settlement(BaseModel):
    '''运输台账模型类'''
    car_id = models.IntegerField(blank=True, null=True, verbose_name='车辆id')
    car_number = models.IntegerField(blank=True, null=True, verbose_name='车牌编号')
    car_name = models.CharField(max_length=20, verbose_name='车牌号')
    payee = models.CharField(max_length=20, verbose_name='收款人')
    destination = models.TextField(verbose_name='目的地')
    transportation_time = models.TextField(verbose_name='运输时间')
    settlement_number = models.TextField(verbose_name='结算单号')
    total_freight = models.FloatField( verbose_name='总运费')
    buckle_oil = models.FloatField( null=True, blank=True, verbose_name='扣油')
    demand_for_cost = models.FloatField( null=True, blank=True, verbose_name='车主应进费用')
    ETC_cost = models.FloatField(null=True, blank=True, max_length=20, verbose_name='ETC费用')
    other_cost = models.FloatField(null=True, blank=True, max_length=20, verbose_name='其他费用')
    labor_ticket_amount = models.FloatField(null=True, blank=True, max_length=20, verbose_name='应开劳务票金额')
    taxation_for_bank = models.FloatField( null=True, blank=True, max_length=20, verbose_name='应交税费（转银行卡）')
    taxation_for_wechat = models.FloatField( null=True, blank=True, max_length=20, verbose_name='应交税费（转微信）')
    remarks = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        db_table = 'settlement'
        verbose_name = '运费结算'
        verbose_name_plural = verbose_name




