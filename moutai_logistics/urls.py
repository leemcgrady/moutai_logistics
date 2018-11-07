from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^xadmin/', xadmin.site.urls),
    url(r'^', include(('car.urls', 'car'), namespace='car')), # 商品模块
]

# from django.urls import path
# from django.conf.urls import include, url
# from django.contrib import admin
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'', include(('learning_logs.urls', "learning_logs"), namespace="learning_logs")),
# ]