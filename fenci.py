#encoding=utf-8
import jieba
f = open("D:\\222AI\\erclassification\\icedoc.txt","w") #读取文本
f1 = f.read()
seg_list = jieba.cut(f1, cut_all=True)
f.write(seg_list)
f.close()
print ("Full Mode:", "/ ".join(seg_list) ) # 全模式
seg_list = jieba.cut("我来到u北京清华大学", cut_all=False)
print ("Default Mode:", "/ ".join(seg_list) ) # 精确模式
seg_list = jieba.cut("戴尔公司将于５月１８日公布第一季度的财报。")  # 默认是精确模式
print (", ".join(seg_list))
seg_list = jieba.cut_for_search("你们好，市场竞争我是涂斌琴")  # 搜索引擎模式
print( ", ".join(seg_list))

