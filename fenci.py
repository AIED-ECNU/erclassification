#encoding=utf-8
import jieba
import jieba.analyse
import sys
import codecs
# f = open("icedoc.txt","r") #读取文本
# for w in f:
#     print(w)
# f.close()
# seg_list = jieba.cut_for_search(f)
# f.write("")
# print ( "/ ".join(seg_list) )
with open('icedoc.txt', 'r') as f:
    print(f.readlines())
    w = f.read()
for line in f.readlines():
        print(line.strip())
seg_list = jieba.cut_for_search(w)
print ( "/ ".join(seg_list) )
stoplist = {}.fromkeys([ line.strip() for line in open("stopword.txt") ])
#stoplist = codecs.open('stopword.txt','r',encoding='utf8').readlines()如果文件不是utf8编码

