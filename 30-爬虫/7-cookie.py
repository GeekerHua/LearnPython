import urllib2
import urllib

headers = {
    "Host": "www.baidu.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Encoding": "UTF-8",
    # "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cookie": "BAIDUID=27EABD5D9A17098DE9866249B33B7D0C:FG=1; BIDUPSID=27EABD5D9A17098DE9866249B33B7D0C; PSTM=1478695188; BDUSS=0pWckd-Y1VkZGZBTXZCcllGcGplZklNNVVSVUNCZzFlU2Uyd3pPcy16eHh4SVJZSVFBQUFBJCQAAAAAAAAAAAEAAADlLXQOx-~LrrrswdYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHE3XVhxN11YQ; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=1; BD_HOME=1;H_PS_PSSID=1420_21098_22582; BD_UPN=123253; sugstore=0",
}

url = 'https://www.baidu.com/'
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

print response.read()  # .decode('utf8')
