from django.urls import path
from .views import average

urlpatterns = [
    path('average/', average, name='average'),
]