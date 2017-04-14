#!/usr/bin/env python
# coding=utf-8

import urllib2
import urllib
import random

# 1.直接请求

# # 向指定的url发送请求
# response = urllib2.urlopen("http://www.baidu.com/")

# # 服务器返回对象的类文件对象支持python文件操作
# html = response.read()
list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36']
# print html
user_agent = random.choice(list)

# 2.使用resquest
user_head = {'User-Agent': user_agent}

request = urllib2.Request("http://www.baidu.com/", headers=user_head)
word = {'wd': '传智'}
newWord = urllib.urlencode(word)


# request.add_header('Connection', 'keep-alive')

# 只有第一个字母大写，其他都是小写
# print request.get_header('User-agent')

response = urllib2.urlopen(request)

print response.read()
# print response.getcode()
# print response.geturl()
# print response.info()
