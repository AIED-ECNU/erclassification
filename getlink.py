# coding=utf-8
import urllib.request
import re
from bs4 import BeautifulSoup

url_list = []
for page in range(1,8):
    url = 'http://www.eduxiao.com/zuowen1/list_1_' + str(page) + '.html'
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "lxml")
    url_all = soup.find_all(class_="title")  # 找到超链接所在位置
    # 获取<a href></a>中的URL
    for each in url_all:
        if str(each.get('href'))[:4] == 'http':    # get each中“href”的部分，在href中遇到了‘http’这4个字符，就取出来
            f = open("grade1/grade1_links.txt", "a+")  # 把各个年级的链接写进文档中
            f.write(each.get('href') + '\n')
f.close()

print('end')




