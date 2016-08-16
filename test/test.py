# coding=utf-8
import cookielib
import urllib2, bs4,re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs4.BeautifulSoup(html_doc, 'html.parser', from_encoding='uft-8')

print '获取所有的链接'
links = soup.find_all('a')

for link in links:
    print link.name + '\n', link['href'] + '\n', link.get_text()
print 'lacie'
l = soup.find('a', href='http://example.com/lacie')
print l.name + '\n', l['href'] + '\n', l.get_text()

print '正则表达式匹配'
link_node = soup.find('a',href=re.compile(r'ill'))
print link_node.name + '\n', link_node['href'] + '\n', link_node.get_text()


# url = "http:www.baidu.com"
# print '第一种方法'
#
# response1 = urllib2.urlopen(url)
#
# print response1.getcode()
# print len(response1.read())
#
# print '第二种方法'
#
# request = urllib2.Request(url)
# request.add_header("user-agent", "Mozilla/5.0")
#
# response2 = urllib2.urlopen(url)
#
# print response2.getcode()
# print len(response2.read())
#
# print '第三种方法'
#
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# urllib2.install_opener(opener)
#
# response3 = urllib2.urlopen(url)
#
# print response3.getcode()
# print response3.read()
# print cj
