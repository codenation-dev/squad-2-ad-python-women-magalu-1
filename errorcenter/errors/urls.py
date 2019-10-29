from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.user_login, name='user-login'),
    path('register/', views.user_register, name='user-register'),
    path('list/', views.error_list, name='error-list'),
    path('detail/<int:error_id>/', views.error_detail, name='error-detail'),
]
