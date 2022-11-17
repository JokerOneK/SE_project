from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("hospital.urls")),
    path('admintest/', admin.site.urls),
]
