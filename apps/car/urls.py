from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
# from user import views
from car.views import IndexView
# from itsdangerous import TimedJSONWebSignatureSerializer
# from user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView
# from django.contrib.auth.views import login from . import views
urlpatterns = [
    # url(r'^register$', views.register, name='register'), # 注册

    url(r'^$', IndexView.as_view(), name='index'),
]

app_name = "car"


