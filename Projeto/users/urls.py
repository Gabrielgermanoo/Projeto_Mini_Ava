from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView

from .views import UsuarioCreate, PerfilUpdate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'users/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name = 'registrar'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name = 'atualizar-dados'),
    path('change-password/', PasswordChangeView.as_view(template_name = 'users/change_pass.html'), name='change_password'), 
]