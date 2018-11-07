from django.contrib import admin
from car.models import Car, CarTransportLedger
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
    actions = ["save_execl"]

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
                # eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
                # operation_time = operation_time.datetime.Asia().replace(tzinfo=utc)
                print(operation_time)
                problem_registration = obj.problem_registration
                w.write(excel_row, 0, '')
                w.write(excel_row, 1, car_name)
                is_open = ''
                is_close = ''
                if state == 0:
                    is_close = '√'
                else:
                    is_open = '√'
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


admin.site.register(Car, CarAdmin)
admin.site.register(CarTransportLedger, CarTransportLedgerAdmin)
