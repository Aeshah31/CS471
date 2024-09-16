from django.urls import path
from .views import views  # تأكد من استيراد الدالة الصحيحة

urlpatterns = [
    path('', views, name='views'),  # استخدم الاسم الصحيح هنا
]