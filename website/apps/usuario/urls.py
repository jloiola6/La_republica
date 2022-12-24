from django.contrib.auth import views as auth_views

from django.urls import path, reverse_lazy

from apps.usuario.views import *

app_name = 'usuario'

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),    
    path('editar-dados/', editar_dados, name='editar-dados'),    
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
    #Recuperar conta
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usuario/resetar-senha/comfirmar-resetar-senha.html', success_url = reverse_lazy('usuario:password_reset_complete')),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='usuario/resetar-senha/password_reset_complete.html'), name='password_reset_complete'),

    path('perfil/<int:perfil_id>', perfil, name='perfil'),
    path('menu-perfil', menu_perfil, name='menu-perfil'),
    path('usuarios', usuarios, name='usuarios'),
]
