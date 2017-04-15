# coding=utf-8
import re
import urllib2


class Spider:
    def __init__(self):
        self.page = 1
        self.url = 'http://www.neihan8.com/article/list_5_'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
        self.switch = True

    def loadPage(self):
        url = self.url + str(self.page) + '.html'
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        self.dealPage(response.read())

    def dealPage(self, html):
        pattern = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)
        result = pattern.findall(html)
        with open('duanzi.txt', 'a') as f:
            for item in result:
                self.saveItem(item.decode('gbk').encode('utf8'), f)

    def saveItem(self, item, f):
        print '正在写入段子……'
        pattern = re.compile(r'(?:<.*?>)|(?:&.*?;)')
        item = pattern.sub('', item.strip())
        pattern2 = re.compile(r'(\n+\s*\n*)|(\s+)')
        item = pattern2.sub('\n', item)
        print item
        f.write(item + '\n\n')

    def start(self):
        while self.switch:
            self.loadPage()
            inputStr = raw_input('是否继续抓取：Enter，退出：Q:')
            if inputStr == 'Q':
                self.switch = False
                print '感谢使用'
            self.page += 1


if __name__ == '__main__':
    duanziSpider = Spider()
    duanziSpider.start()
