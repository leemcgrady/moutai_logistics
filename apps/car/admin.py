from django.contrib import admin
from car.models import Car, CarTransportLedger, Settlement
from django.http import HttpResponse
from xlwt import *
import os
from io import StringIO, BytesIO
import datetime
import pytz
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


# car_name = models.CharField(max_length=20, verbose_name='车牌号')
# owner_name = models.CharField(max_length=20, null=True, verbose_name='车主姓名')
# owner_phone = models.CharField(max_length=11, null=True, verbose_name='车主电话')
# driver_name = models.CharField(max_length=20, null=True, verbose_name='驾驶员姓名')
# driver_phone = models.CharField(max_length=11, null=True, verbose_name='驾驶员电话')
class CarAdmin(admin.ModelAdmin):
    fields = ('car_name', 'owner_name', 'owner_phone', 'driver_name', "driver_phone")
    list_display = ('car_name', 'owner_name', 'owner_phone', 'driver_name', 'driver_phone')
    search_fields = ('car_name', )
    list_per_page = 20
    actions = ["save_execl", 'add_num']

    def add_num(self, request, queryset):

        settlement_list = Settlement.objects.all()

        for settlement in settlement_list:
            for obj in queryset:
                if settlement.car_name == obj.car_name:
                    print('---%s---' % obj.car_name)
                    if settlement.car_number != 0:
                        obj.car_number = settlement.car_number
                    else:
                        obj.car_number = None

                    obj.save()


    def save_execl(self, request, queryset):
        """
        导出excel表格
        """
        if queryset:
            # 创建工作薄
            ws = Workbook(encoding='utf-8')
            w = ws.add_sheet(u"数据报表第一页")
            w.write(0, 0, "id")
            w.write(0, 1, u"车牌号")
            w.write(0, 2, u"车主")
            w.write(0, 3, u"电话")
            w.write(0, 4, u"驾驶员")
            w.write(0, 5, u"电话")
            # 写入数据
            excel_row = 1
            for obj in queryset:
                car_id = obj.id
                car_name = obj.car_name
                owner_name = obj.owner_name
                owner_phone = obj.owner_phone
                driver_name = obj.driver_nameimport
                driver_phone = obj.driver_phone
                print(owner_name)
                w.write(excel_row, 0, car_id)
                w.write(excel_row, 1, car_name)
                w.write(excel_row, 2, owner_name)
                w.write(excel_row, 3, owner_phone)
                w.write(excel_row, 4, driver_name)
                w.write(excel_row, 5, driver_phone)
                excel_row += 1
            # 检测文件是够存在
            # 方框中代码是保存本地文件使用，如不需要请删除该代码
            ###########################
            exist_file = os.path.exists("test.xls")
            if exist_file:
                os.remove(r"test.xls")
            ws.save("test.xls")
            ############################
            sio = BytesIO()
            ws.save(sio)
            sio.seek(0)
            response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=test.xls'
            response.write(sio.getvalue())
            return response

    save_execl.short_description = "导出Excel"  # 按钮显示名字
    add_num.short_description = "添加编号"  # 按钮显示名字


# car = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='操作车辆')
# state = models.SmallIntegerField(default=0, choices=status_choices, verbose_name='施解封状态')
# location = models.CharField(max_length=11, null=True, verbose_name='地点')
# operation_time = models.DateTimeField(default=timezone.now,verbose_name='操作时间')
# problem_registration = models.CharField(max_length=256, verbose_name='问题登记')
class CarTransportLedgerAdmin(admin.ModelAdmin):

    fields = ('car_name', 'state', 'location', 'operation_time', "problem_registration")
    list_display = ('car_name', 'state', 'location', 'operation_time', 'problem_registration')
    # list_editable = ('car', 'state', 'location', 'operation_time', 'problem_registration')
    date_hierarchy = 'operation_time'
    list_per_page = 20
    actions = ["save_execl"]
    search_fields = ('car_name', )

    def add_view(self, request, form_url='', extra_context=None):
        return super().add_view(request)

    def save_model(self, request, obj, form, change):
        car_info = Car.objects.get(car_name__contains=obj.car_name)
        obj.car_id = car_info.id
        obj.save()

    def car_name(self, obj):
        return obj.car.car_name

    def save_execl(self, request, queryset):
        """
        导出excel表格
        """
        if queryset:
            # 创建工作薄
            ws = Workbook(encoding='utf-8')
            w = ws.add_sheet(u"数据报表第一页")
            w.write(0, 0, u"操作人员")
            w.write(0, 1, u"车牌号")
            w.write(0, 2, u"施封")
            w.write(0, 3, u"解封")
            w.write(0, 4, u"地点")
            w.write(0, 5, u"时间")
            w.write(0, 6, u"问题登记")
            # 写入数据
            excel_row = 1
            for obj in queryset:
                car_name = obj.car_name
                state = obj.state
                location = obj.location
                operation_time = str(obj.operation_time)
                problem_registration = obj.problem_registration
                is_open = ''
                is_close = ''
                if state == 0:
                    is_close = '√'
                else:
                    is_open = '√'
                w.write(excel_row, 0, '')
                w.write(excel_row, 1, car_name)
                w.write(excel_row, 2, is_close)
                w.write(excel_row, 3, is_open)
                w.write(excel_row, 4, location)
                w.write(excel_row, 5, operation_time)
                w.write(excel_row, 6, problem_registration)
                excel_row += 1
            # 检测文件是够存在
            # 方框中代码是保存本地文件使用，如不需要请删除该代码
            ###########################
            exist_file = os.path.exists("test.xls")
            if exist_file:
                os.remove(r"test.xls")
            ws.save("test.xls")
            ############################
            sio = BytesIO()
            ws.save(sio)
            sio.seek(0)
            response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=test.xls'
            response.write(sio.getvalue())
            return response

    save_execl.short_description = "导出Excel"  # 按钮显示名字


class SettlementAdmin(admin.ModelAdmin):

    # fields = ('car_number', 'car_name', 'payee', 'destination',
    #           "transportation_time", 'settlement_car_number', 'total_freight',
    #           'buckle_oil', 'ETC_cost', 'other_cost', 'remarks')
    fieldsets = [
        (None, {'fields': ['car_number', 'car_name', 'payee']}),
        ('------', {'fields': ['transportation_time']}),
    ]
    list_display = ('car_number', 'car_name', 'payee', 'destination',
              "transportation_time", 'settlement_number', 'total_freight',
              'buckle_oil', 'demand_for_cost', 'ETC_cost', 'other_cost', 'labor_ticket_amount', 'taxation_for_bank',
              'taxation_for_wechat', 'remarks')
    actions = ["save_execl"]
    search_fields = ('car_number', 'settlement_number')

    #存储运输台账
    def save_model(self, request, obj, form, change):
        car_info = Car.objects.get(car_name__contains=obj.car_name)
        obj.car_id = car_info.id
        obj.car_name = car_info.car_name
        gongshi1 = 0.0520388
        gongshi2 = 0.999
        total_freight = obj.total_freight
        buckle_oil = obj.buckle_oil
        demand_for_cost = total_freight - buckle_oil
        ETC_cost = obj.ETC_cost
        other_cost = obj.other_cost
        labor_ticket_amount = demand_for_cost - ETC_cost - other_cost
        taxation_for_bank = labor_ticket_amount * gongshi1
        taxation_for_wechat = taxation_for_bank / gongshi2

        obj.demand_for_cost = '%.2f' % demand_for_cost
        obj.labor_ticket_amount = '%.2f' % labor_ticket_amount
        obj.taxation_for_bank = '%.2f' % taxation_for_bank
        obj.taxation_for_wechat = '%.2f' % taxation_for_wechat

        obj.save()

    def save_execl(self, request, queryset):
        """
        导出excel表格
        """
        if queryset:
            # 创建工作薄
            ws = Workbook(encoding='utf-8')
            w = ws.add_sheet(u"数据报表第一页")
            w.write(0, 0, u"编号")
            w.write(0, 1, u"车号")
            w.write(0, 2, u"收款人")
            w.write(0, 3, u"目的地")
            w.write(0, 4, u"运输时间")
            w.write(0, 5, u"结算单号")
            w.write(0, 6, u"总运费")
            w.write(0, 7, u"扣油")
            w.write(0, 8, u"车主应进费用")
            w.write(0, 9, u"ETC费用")
            w.write(0, 10, u"其他费用")
            w.write(0, 11, u"应开劳务票金额")
            w.write(0, 12, u"应交税费（转银行卡）")
            w.write(0, 13, u"应交税费（转微信）")
            w.write(0, 14, u"备注")
            # 写入数据
            excel_row = 1
            for obj in queryset:

                w.write(excel_row, 0, obj.car_number)
                w.write(excel_row, 1, obj.car_name)
                w.write(excel_row, 2, obj.payee)
                w.write(excel_row, 3, obj.destination)
                w.write(excel_row, 4, obj.transportation_time)
                w.write(excel_row, 5, obj.settlement_number)
                w.write(excel_row, 6, obj.total_freight)
                w.write(excel_row, 7, obj.buckle_oil)
                w.write(excel_row, 8, obj.demand_for_cost)
                w.write(excel_row, 9, obj.ETC_cost)
                w.write(excel_row, 10, obj.other_cost)
                w.write(excel_row, 11, obj.labor_ticket_amount)
                w.write(excel_row, 12, obj.taxation_for_bank)
                w.write(excel_row, 13, obj.taxation_for_wechat)
                w.write(excel_row, 14, obj.remarks)
                excel_row += 1
            # 检测文件是够存在
            # 方框中代码是保存本地文件使用，如不需要请删除该代码
            ###########################
            exist_file = os.path.exists("test.xls")
            if exist_file:
                os.remove(r"test.xls")
            ws.save("test.xls")
            ############################
            sio = BytesIO()
            ws.save(sio)
            sio.seek(0)
            response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=test.xls'
            response.write(sio.getvalue())
            return response

    save_execl.short_description = "导出Excel"  # 按钮显示名字

    # class Ugg(admin.SimpleListFilter):
    #     title = _('decade born')
    #     parameter_name = 'xxxxxx'
    #
    #     def lookups(self, request, model_admin):
    #         """
    #         显示筛选选项
    #         :param request:
    #         :param model_admin:
    #         :return:
    #         """
    #         return models.UserGroup.objects.values_list('id', 'title')
    #
    #     def queryset(self, request, queryset):
    #         """
    #         点击查询时，进行筛选
    #         :param request:
    #         :param queryset:
    #         :return:
    #         """
    #         v = self.value()
    #         return queryset.filter(ug=v)
    #
    # list_filter = ('user', Ugg,)


admin.site.register(Car, CarAdmin)
admin.site.register(CarTransportLedger, CarTransportLedgerAdmin)
admin.site.register(Settlement, SettlementAdmin)
