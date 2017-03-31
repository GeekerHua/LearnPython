from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^fwb/$', views.fwb),
    url(r'^fwbShow/$', views.fwbShow),
    url(r'^jiansuo/$', views.jiansuo),
    url(r'^hello/$', views.hello),
]
