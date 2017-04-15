# coding=utf-8
from bs4 import BeautifulSoup as bs
import urllib2

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
request = urllib2.Request('http://hr.tencent.com/position.php?&start=10', headers=headers)

html = urllib2.urlopen(request).read()

soup = bs(html, 'lxml')
odd = soup.select('.odd')
even = soup.select('.even')

selector = odd + even 

for item in selector:
    positionName = item.select("td a")[0].get_text()
    positionLink = item.select("td a")[0].attrs["href"]
    positionType = item.select("td")[1].get_text()
    positionNum = item.select("td")[2].get_text()
    positionAddr = item.select("td")[3].get_text()
    positionTime = item.select("td")[4].get_text()
    print positionName
