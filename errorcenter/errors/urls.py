from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.user_login, name='user-login'),
    path('register/', views.user_register, name='user-register'),
    path('home/<token>', views.error_list, name='home-page'),
    path('logout/', views.deslogar_usuario, name='deslogar_usuario')
]
