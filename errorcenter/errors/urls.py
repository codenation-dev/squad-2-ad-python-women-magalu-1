from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.user_login, name='user-login'),
    path('register/', views.user_register, name='user-register'),
    path('home/', views.error_list, name='home-page'),
]
