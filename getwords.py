# coding=utf-8
import urllib.request
import re
from bs4 import BeautifulSoup

url_list = []
for page in range(1, 8):
    url = 'http://www.eduxiao.com/zuowen1/list_1_' + str(page) + '.html'
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "lxml")
    url_all = soup.find_all(class_="title")  # 找到超链接所在位置
    # 获取<a href></a>中的URL
    for each in url_all:
        if str(each.get('href'))[:4] == 'http':  # get each中“href”的部分，在href中遇到了‘http’这4个字符，就取出来
            url_list.append(each.get('href'))  # 加入url_list这个列表中
for i in range(1,len(url_list)):
    # print(url_list[1])
    url = url_list[i]
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "lxml")
    title = soup.find_all(class_="title")  # 找到作文所在位置
    for word in title:
        title1 = word.get_text('|', strip='True')  # 用get_text的方法获得爬虫内容
    filepath = title1 + '.txt'
    print(filepath)
    article = soup.find_all(class_="content")  # 找到作文所在位置
    for word in article:
        words = word.get_text('|', strip='True')  # 用get_text的方法获得爬虫内容
        print(words)
    f = open("grade1/" + filepath, "w")
    f.write(words.encode('gbk','ignore').decode('gbk'))
    f.close()


# url = "http://www.eduxiao.com/zuowen1/85620.html"
# with open('filepath', 'w') as f:#写进文档
#     f.write(words)



