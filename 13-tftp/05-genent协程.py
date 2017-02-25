#!/usr/bin/env python
# coding=utf-8

'''
# Author = GeekerHua
# 2017.02.10 16:30:56
'''

import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        # 这个sleep要用gevent中的sleep才行
        gevent.sleep(1)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()

