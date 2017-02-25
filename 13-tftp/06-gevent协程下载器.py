#!/usr/bin/env python
# coding=utf-8

'''
# Author = GeekerHua
# 2017.02.10 16:37:09
'''
from gevent import monkey;
import gevent
import urllib2

# 有IO才做是需要这句话
monkey.path_all()

def myDownLoad(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    