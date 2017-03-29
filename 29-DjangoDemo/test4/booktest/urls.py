from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^bianliang/$', views.bianliang),
    url(r'^biaoqian/$', views.biaoqian),
    url(r'^guolvqi/$', views.guolvqi),
    url(r'^jicheng/$', views.jicheng),
    url(r'^zhuanyi/$', views.zhuanyi),
    url(r'^csrf1/$', views.csrf1),
    url(r'^csrf2/$', views.csrf2),
]
