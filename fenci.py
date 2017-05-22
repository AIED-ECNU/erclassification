#encoding=utf-8
import jieba.analyse  #导入结巴分词包
with open('stopword.txt', 'r') as f:
    stopwords = f.read()  # 打开stopword（停用词）文件
with open('icedoc.txt', 'r') as f:
    w = f.read()  #读取要分词的文件
    seg1 = jieba.cut_for_search(w)  #进行分词
    final = []  # 设置一个变量
    for seg_list in seg1:
        if seg_list not in stopwords:
            final.append(seg_list)  # 对第一次分词的结果进行处理，去掉停用词
seg_final=" ".join(final)  #用空格符号分隔词语
with open('icedoc1.txt', 'w') as f:
    f.write(seg_final)#将最终的分词结果写进另外文档



