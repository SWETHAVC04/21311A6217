from django.contrib import admin
from django.urls import path, include
from myapp.views import average

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('', average, name='home'),
]

