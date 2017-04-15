import urllib2

url = 'http://192.168.12.79'

user = 'bigcat'
passwd = '123456'

passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

passwdmgr.add_password(None, url, user, passwd)

httpauto_hander = urllib2.HTTPBasicAuthHandler(passwdmgr)

opener = urllib2.build_opener(httpauto_hander)

response = opener.open(url)

print response.read()
