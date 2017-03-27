# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # 匹配index首页
    url(r'^$', views.index),
    # 位置参数，使用正则自带的分组小括号
    # url(r'^(\d+)_(\w+)/$', views.show),
    # 参数命名，使用正则自带的分组命名
    url(r'^(?P<id>\d+)_(?P<title>\w+)/$', views.show),
    url(r'^m1/$', views.method1),
    url(r'^m2/$', views.method2),
    url(r'^m3/$', views.method3),

    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),
    url(r'^get3/$', views.get3),
    url(r'^post1/$', views.post1),
    url(r'^post2/$', views.post2),

    url(r'^json1/$', views.json1),
    url(r'^json2/$', views.json2),
    url(r'^redirect1/$', views.redirect1),
    url(r'^cookie_test/$', views.cookie_test),
    url(r'^session_test/$', views.session_test),
]
