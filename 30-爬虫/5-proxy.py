import urllib2

proxy = {'http': '124.88.67.19:80'}

httpproxy_hander = urllib2.ProxyHandler(proxy)


opener = urllib2.build_opener(httpproxy_hander)

request = urllib2.Request('http://www.baidu.com')

response = opener.open(request)

print response.read().decode('gbk')
