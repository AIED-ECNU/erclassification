# coding=utf-8
import urllib.request
import re
from bs4 import BeautifulSoup

url_list = []
f = open('grade2/grade2_links.txt','r')
for i in f.readlines():
    url_list.append(i)
f.close()
print(url_list)
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
    f = open("grade2/" + filepath, "w")
    f.write(words.encode('gbk','ignore').decode('gbk'))
    f.close()


# url = "http://www.eduxiao.com/zuowen1/85620.html"
# with open('filepath', 'w') as f:#写进文档
#     f.write(words)



