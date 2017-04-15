# coding=utf-8
import urllib2
from lxml import etree
import urllib
# 获取每页帖子的url


def loadData(url):
    proxy = {'http': '110.73.38.191:8123'}
    # proxy = {'http': '221.5.6.102:8080'}
    httpproxy_hander = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(httpproxy_hander)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
    request = urllib2.Request(url)
    response = opener.open(request)
    return response.read()


def loadPage(url):
    html = loadData(url)
    with open("a.html", 'w') as f:
        f.write(html)
    # print html
    content = etree.HTML(html)
    link_list = content.xpath(
        '//div[@class="t_con cleafix"]/div/div/div/a/@href')
    # link_list = content.xpath('//div')
    # link_list = content.xpath(
    #     '//div[@class="threadlist_lz clearfix"]/div/a/@href')
    # print link_list
    for link in link_list:
        dealPage(loadData('http://tieba.baidu.com' + link))


def dealPage(html):
    content = etree.HTML(html)
    imageLink_list = content.xpath('//img[@class="BDE_Image"]/@src')
    for link in imageLink_list:
        writeImage(loadData(link), link[-10:])


def writeImage(data, name):
    print '正在写入图片---' + name
    with open('img/' + name, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    # name = raw_input("请输入需要爬取的贴吧:")
    name = '美女'
    kw = {'kw': name}
    newkw = urllib.urlencode(kw)
    url = 'http://tieba.baidu.com/f?' + newkw
    loadPage(url)
