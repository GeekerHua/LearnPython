from lxml import etree
import json

html = etree.HTML('hello.html')
result = html.xpath('//tr/td[@data-title="IP"]')

lists = [x.text for x in result]
print json.dumps(lists, indent=4)
