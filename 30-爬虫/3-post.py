import urllib2
import urllib
import ssl
# 忽略未经CA认证的ssl错误
# context = ssl._create_unverified_context

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

formdata = {
    "type": "AUTO",
    "i": "i love you",
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF - 8",
    "action": "FY_BY_CLICKBUTTON",
    "typoResult": "true"
}
data = urllib.urlencode(formdata)
request = urllib2.Request(url, headers=header, data=data)
# print request.get_method()
response = urllib2.urlopen(request)

print response.read()
