# coding=utf-8
import urllib.request
import re
from bs4 import BeautifulSoup

url_list = []
for page in range(1,46):
    url = 'http://www.eduxiao.com/zuowen6/list_6_' + str(page) + '.html'
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "lxml")
    url_all = soup.find_all(class_="title")  # 找到超链接所在位置
    # 获取<a href></a>中的URL
    for each in url_all:
        if str(each.get('href'))[:4] == 'http':  # get each中“href”的部分，在href中遇到了‘http’这4个字符，就取出来
            url_list.append(each.get('href'))  # 加入url_list这个列表中

f = open("grade6/grade6_links" , "w")# 把各个年级的链接写进文档中
f.write(repr(url_list))
f.close()
print(url_list)
print('end')




