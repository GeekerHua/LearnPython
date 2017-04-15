import urllib2
import cookielib

fileName = 'cookie.txt'
# cookiejar = cookielib.CookieJar()
cookiejar = cookielib.MozillaCookieJar(fileName)

cookie_hander = urllib2.HTTPCookieProcessor(cookiejar)

opener = urllib2.build_opener(cookie_hander)

request = urllib2.Request('http://www.baidu.com')

response = opener.open(request)

# 保存cookie到本地
cookiejar.save()
# 读取cookie
# cookiejar.load()

cookies = ''
for item in cookiejar:
    cookies = cookies + item.name + '=' + item.value + ';'

print cookies
print '*' * 20
print cookiejar
