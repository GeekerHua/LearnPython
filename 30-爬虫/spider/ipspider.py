# coding=utf-8
import urllib2
import urllib
import random
import time
import socket
from lxml import etree
import json
import sqlite3


TESTURL = 'http://www.baidu.com'
successProxys = []
coon = sqlite3.connect('spider.db')


def randomProxy():
    return random.choice(successProxys)


def loadPage(url):
    request = urllib2.Request(url, headers={
                              "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
    proxy = {}
    if len(successProxys):
        proxy = randomProxy()
    hander = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(hander)
    request = urllib2.Request(url)
    response = opener.open(request)
    return response


def testProxy(proxy):
    # proxy = {'HTTP': '122.44.55.33:80'}
    # proxy = {}
    # print '正在测试ip:%s' % proxy.values()[0]
    hander = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(hander)

    request = urllib2.Request(TESTURL)
    try:
        response = opener.open(request, timeout=1)
        writeProxy(proxy)
        successProxys.append(proxy)
        # print 'ip:%s可用' % proxy.values()[0]
    except urllib2.HTTPError as err:
        print err.code
    except urllib2.URLError as err:
        print 'errCode = 600'
        print '超时'


def getProxyPage(page):
    url = 'http://www.kuaidaili.com/free/inha/' + page
    content = loadPage(url).read()
    html = etree.HTML(content)
    ips = html.xpath('//tr/td[@data-title="IP"]')
    ports = html.xpath('//tr/td[@data-title="PORT"]')
    schemes = html.xpath('//tr/td[@data-title="类型"]'.decode('utf8'))

    result = zip(ips, ports)
    result = [{z.text: x.text + ':' + y.text}
              for (x, y, z) in zip(ips, ports, schemes)]
    return result


def getProxy():
    totalProxy = []
    totalPage = 100
    for i in range(1, totalPage):
        print '正在抓取第%d页，共%d页, 已抓取可用ip个数%d个' % (i, totalPage, len(totalProxy))
        result = getProxyPage(str(i))
        i += 1
        totalProxy.extend(result)
    else:
        return totalProxy


def writeProxy(proxy):
    scheme = proxy.keys()[0]
    ipp = proxy.values()[0].split(':')
    ip = ipp[0]
    port = ipp[1]
    print 'scheme = %s, ip = %s, port = %s' % (scheme, ip, port)
    count = coon.execute('SELECT count(*) FROM T_PROXY WHERE IP = "%s";' % ip)
    print count
    if count != '1':
        try:
            coon.execute('insert into T_PROXY values (?, ?, ?)',
                         (ip, port, scheme))
            coon.commit()
        except Exception:
            pass


def createDbs():
    coon.execute('''CREATE TABLE IF NOT EXISTS T_PROXY
        (IP TEXT PRIMARY KEY    NOT NULL,
        PORT            TEXT     NOT NULL,
        SCHEME        TEXT   NOT NULL
        );''')
    print "Table created successfully"


if __name__ == '__main__':
    createDbs()
    proxys = getProxy()
    for proxy in proxys:
        testProxy(proxy)
    else:
        coon.close()
        print successProxys
        print '*' * 30
        print '抓取结束，共抓取可用ip %d 个' % len(successProxys)
        # print '共有ip:%d个，可用ip: %d个' %(len(proxys), len(successProxys))
        json.dump(successProxys, open('ips.json', 'w'), indent=4)
    # testProxy('http', '125.92.32.210:808')
