from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^jingtai/$', views.jingtai),
    url(r'^$', views.index),
    url(r'^pic1/$', views.pic1),
    url(r'^pic2/$', views.pic2),
    url(r'^pic3/$', views.pic3),
    url(r'^page(\d*)/$', views.page1),
    url(r'^area1/$', views.area1),
    url(r'^sheng/$', views.sheng),
    url(r'^shi(\d*)/$', views.shi),
]