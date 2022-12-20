from django.contrib.auth import views as auth_views
from django.urls import path

from apps.usuario.views import *

app_name = 'usuario'

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('cadastro', cadastro, name='cadastro'),
    path('perfil', perfil, name='perfil'),
    path('associar-colaborador', associar_colaborador, name='associar-colaborador'),
    path('servico-colaborador', servico_colaborador, name='servico-colaborador'),
    path('associar-adm', associar_adm, name='associar-adm'),
    path('usuarios', usuarios, name='usuarios'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usuario/comfirmar-resetar-senha.html'),name='password_reset_confirm'),
]