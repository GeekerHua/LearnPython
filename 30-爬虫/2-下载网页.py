#!/usr/bin/env python
# coding=utf-8

"""
# Author = GeekerHua
# 2017-04-12 17:54:11
"""

import urllib
import urllib2
import random


def writePage(html, fileName):
    """
    保存网页到本地
    """
    print '正在存储' + fileName
    with open(fileName + '.html', 'w') as ff:
        ff.write(html)
        print '*' * 33


def loadPage(url, fileName):
    list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36']
# print html
    user_agent = random.choice(list)
# 2.使用resquest
    user_head = {'User-Agent': user_agent}
    print '正在下载' + fileName
    request = urllib2.Request(url, headers=user_head)
    response = urllib2.urlopen(request)
    return response.read()


def tiebaSpider(url, begin=0, end=1):
    for page in range(begin, end + 1):
        pn = (page - 1) * 50
        fullUrl = url + '&pn=%d' % pn
        # print fullUrl
        fileName = '第' + str(page) + '页'
        html = loadPage(fullUrl, fileName)
        writePage(html, fileName)


if __name__ == '__main__':
    kw = raw_input('请输入需要爬取的贴吧名:')
    beginPage = int(raw_input("请输入起始页:"))
    endPage = int(raw_input("请输入终止页:"))

    url = 'http://tieba.baidu.com/f?'
    newkw = urllib.urlencode({'kw': kw})
    newUrl = url + newkw

    tiebaSpider(newUrl, beginPage, endPage)
