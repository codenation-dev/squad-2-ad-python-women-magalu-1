from django.conf.urls import url
from django.urls import path
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('login/', views.user_login, name='user-login'),
    path('register/', views.user_register, name='user-register'),
    path('home/', views.error_list, name='home-page'),
    path('logout/', views.deslogar_usuario, name='deslogar-usuario'),
    path('detail/<int:error_id>/', views.error_detail, name='error-detail'),
]
