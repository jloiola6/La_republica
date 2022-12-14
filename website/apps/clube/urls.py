from django.urls import path

from apps.clube.views import *

app_name = 'clube'

urlpatterns = [
    path('', index, name='index'),
    # path('checkout/', checkout, name='checkout'),
    # path('finalizado/', finalizado, name='finalizado'),
]