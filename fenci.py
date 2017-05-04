#encoding=utf-8
import jieba
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print ("Full Mode:", "/ ".join(seg_list) ) # 全模式
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print ("Default Mode:", "/ ".join(seg_list) ) # 精确模式
seg_list = jieba.cut("本报讯 全球最大个人电脑制造商戴尔公司８日说，由于市场竞争激烈，以及定价策略不当，该公司今年第一季度盈利预计有所下降。'\
'消息发布之后，戴尔股价一度下跌近６％，创下一年来的新低。戴尔公司估计，其第一季度收入约为１４２亿美元，每股收益３３美分。此前公司预测当季收入为１４２亿至１４６亿美元，'\
'每股收益３６至３８美分，而分析师平均预测戴尔同期收入为１４５．２亿美元，每股收益３８美分。为抢夺失去的市场份额，戴尔公司一些产品打折力度很大。戴尔公司首席执行官凯文·罗林斯在一份声明中说，'\
'公司在售后服务和产品质量方面一直在投资，同时不断下调价格。戴尔公司将于５月１８日公布第一季度的财报。")  # 默认是精确模式
print (", ".join(seg_list))
seg_list = jieba.cut_for_search("你们好，市场竞争我是涂斌琴")  # 搜索引擎模式
print( ", ".join(seg_list))
