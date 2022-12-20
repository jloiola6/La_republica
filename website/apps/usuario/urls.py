from django.contrib.auth import views as auth_views

from django.urls import path, reverse_lazy

from apps.usuario.views import *

app_name = 'usuario'

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),    
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
    #Recuperar conta
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usuario/resetar-senha/comfirmar-resetar-senha.html', success_url = reverse_lazy('usuario:password_reset_complete')),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='usuario/resetar-senha/password_reset_complete.html'), name='password_reset_complete'),

    path('perfil', perfil, name='perfil'),
    path('associar-colaborador', associar_colaborador, name='associar-colaborador'),
    path('servico-colaborador', servico_colaborador, name='servico-colaborador'),
    path('associar-adm', associar_adm, name='associar-adm'),
    path('usuarios', usuarios, name='usuarios'),
]
