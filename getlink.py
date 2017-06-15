# coding=utf-8
import urllib.request
import re
from bs4 import BeautifulSoup



url = 'http://www.eduxiao.com/zuowen1/'
req = urllib.request.Request(url)
con = urllib.request.urlopen(req)
doc = con.read()
con.close()
doc = doc.decode('GBK')
#  获取网页内的所有超链接
# links = re.findall(r'href\=\"(http\:\/\/[a-zA-Z0-9\.\/]+)\"', doc)
# for a in links:
#     print(a)


#获取<a href></a>中的URL，有用的代码
# print (u'\n获取超链接:')
# res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
# link = re.findall(res_url ,  doc, re.I|re.S|re.M)
# for url in link:
#     print(url)

url = "http://www.eduxiao.com/zuowen1.html"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,"lxml")
links = soup.find_all('a')#找到超链接所在位置
print(links)


