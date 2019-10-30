from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 

from . import views


urlpatterns = [
    url(r'^errors/(?P<pk>[0-9]+)/$', views.ErrorDetailApiView.as_view(), name='error-detail'),
    url(r'^errors/$', views.ErrorListApiView.as_view(), name='error-list'),
    path('token-auth/', obtain_auth_token, name='token_auth')
    url(r'^errors/$', views.ErrorListCreateApiView.as_view(), name='error-list-create'),
]
