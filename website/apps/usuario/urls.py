from django.urls import path

from apps.usuario.views import *

app_name = 'usuario'

urlpatterns = [
    path('login', login, name='index'),
]