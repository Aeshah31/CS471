from django.urls import path, include

urlpatterns = [
    path('users/', include("apps.usermodule.urls")),  # تأكد من أن هذا السطر صحيح
]