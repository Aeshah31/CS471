from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # مسار لوحة التحكم
    path('books/', include("apps.bookmodule.urls")),  # تضمين urls.py من تطبيق bookmodule
    path('users/', include("apps.usermodule.urls")),   # تضمين urls.py من تطبيق usermodule
]