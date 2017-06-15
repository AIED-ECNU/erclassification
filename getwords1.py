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
link_list = []
print (u'\n获取超链接:')
res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
link = re.findall(res_url ,  doc, re.I|re.S|re.M)
for url in link:
    link_list.append(url)
print(link_list)
for each in link_list:
    x = 1
    url = each
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,"lxml")
    article = soup.find_all(class_="content")#找到作文所在位置
    for word in article:
        words = word.get_text('|',strip='True')#用get_text的方法获得爬虫内容
        print(words)
    with open(str(x).txt, 'w') as f:#写进文档
        f.write(words)
        x = x+1



