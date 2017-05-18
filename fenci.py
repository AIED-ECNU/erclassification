#encoding=utf-8
import jieba.analyse
import re
with open('icedoc.txt', 'r') as f:
    #print(f.readlines())
    w = f.read()
seg_list = jieba.cut_for_search(w)
x= "/".join(seg_list)
# y = re.sub(u"[\uFF0C]","/",x)
with open('icedoc1.txt', 'w') as f:
    f.write(x)
# stoplist = {}.fromkeys([ line.strip() for line in open("stopword.txt") ])
#stoplist = codecs.open('stopword.txt','r',encoding='utf8').readlines()如果文件不是utf8编码

