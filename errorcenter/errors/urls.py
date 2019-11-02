from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.user_login, name='user-login'),
    path('register/', views.user_register, name='user-register'),
    path('home/', views.error_list, name='home-page'),
    path('logout/', views.deslogar_usuario, name='deslogar-usuario'),
    path('detail/<int:error_id>/', views.error_detail, name='error-detail'),
    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/change/',
         auth_views.PasswordChangeView.as_view(template_name='password_reset/password_reset_change.html'),
         name='password_change'),
    path('password_reset/change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_reset_change_done.html'),
         name='password_change_done'),
    path('password_reset/successfull/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
]
