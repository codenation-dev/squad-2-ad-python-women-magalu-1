from django.conf.urls import url
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token 
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^errors/(?P<pk>[0-9]+)/archive/$', views.ErrorArchiveApiView.as_view(), name='error-archive'),
    url(r'^errors/(?P<pk>[0-9]+)/delete/$', views.ErrorDeleteApiView.as_view(), name='error-archive'),
    url(r'^errors/(?P<pk>[0-9]+)/$', views.ErrorDetailApiView.as_view(), name='error-detail'),
    url(r'^errors/$', views.ErrorListCreateApiView.as_view(), name='error-list-create'),
    url(r'^users/$', views.UserCreateApiView.as_view(), name='user-create'),
    path('token-auth/', obtain_auth_token, name='token_auth'),
    path('reset_password/', auth_views.PasswordChangeView.as_view(template_name='password_reset.html', success_url='/login'), name='reset-password'),
]
