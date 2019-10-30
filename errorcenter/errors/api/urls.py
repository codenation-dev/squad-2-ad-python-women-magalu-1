from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^errors/(?P<pk>[0-9]+)/$', views.ErrorDetailApiView.as_view(), name='error-detail'),
    url(r'^errors/$', views.ErrorListCreateApiView.as_view(), name='error-list-create'),
]
