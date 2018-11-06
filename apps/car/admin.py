from django.contrib import admin
from car.models import Car, CarTransportLedger

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


# car = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='操作车辆')
# state = models.SmallIntegerField(default=0, choices=status_choices, verbose_name='施解封状态')
# location = models.CharField(max_length=11, null=True, verbose_name='地点')
# operation_time = models.DateTimeField(default=timezone.now,verbose_name='操作时间')
# problem_registration = models.CharField(max_length=256, verbose_name='问题登记')
class CarTransportLedgerAdmin(admin.ModelAdmin):
    fields = ('car', 'state', 'location', 'operation_time', "problem_registration")
    list_display = ('car', 'state', 'location', 'operation_time', 'problem_registration')
    list_editable = ('car', 'state', 'location', 'operation_time', 'problem_registration')
    date_hierarchy = 'operation_time'
    # prepopulated_fields = {"�car": ("user", "pwd",)}
    list_per_page = 20
# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(CarTransportLedger)
