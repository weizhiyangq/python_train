# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:18:12 2018

@author: YWZQ
"""
import jieba

raw_corpus=["春节电影院是爆满人的",
            "很多人去看电影",
            "电影是个不错的选择",
            "红海行动",
            "今年有很多好看的电影",
            "好看",
            "什么电影好"]

jieba.add_word('红海行动')

raw_list=[]

#汉语分词，jieba
for text in raw_corpus:
    seg_list=jieba.cut(text,cut_all=False,HMM=False)
    wen=' '.join(seg_list)
    #print(wen)
    raw_list.append(wen)
print("law_list",raw_list)
texts = [[word for word in text.split()]
          for text in raw_list]
print(texts)

#为各词语分配id等
from gensim import corpora
dictionary = corpora.Dictionary(texts)#为得到的单词表进行唯一性操作，得到无重复的单词字典
print('词典：',dictionary)
for i in dictionary:
    print(i,dictionary[i])
print(dictionary.token2id)#无重复的单词及对应id列表
bow_corpus = [dictionary.doc2bow(text) for text in texts]
print("各句出现在词库中的词及个数:",bow_corpus)

new_doc = "电影红海行动是好看的"#准备检测用的文档
new_doc=jieba.cut(new_doc)
new_doc=' '.join(new_doc)
new_vec = dictionary.doc2bow(new_doc.split())
print ("检测新语句词语id及个数：",new_vec) #显示检测文档单词id及个数，id对应在上述语料库得到的个数超过1的单词id，若检测文档的单词未在id表中出现，则不显示


#显示权重，词语重要性排序实验
from gensim import models
tfidf = models.TfidfModel(bow_corpus)

string = "红海行动是好看的电影"
string=jieba.cut(string)
string=' '.join(string)
string_bow = dictionary.doc2bow(string.split())#得到system和minors的id和个数
string_tfidf = tfidf[string_bow]#由于system在上面的语料库中出现4次，而minors2次，说明system是更常见的词，所以重要性小，但是，如果将system在需检测的文档中的出现次数提高，也可将他的重要性提高
print ('新语句各词语在语库词的id及个数:',string_bow)  
print ('新语句各词语在语库中的id及重要度tfidf:',string_tfidf)#得到一个列表，列表里是各个元组，元组包括id和重要度

for i in range(len(string_tfidf)):
    print('单纯显示重要度tfidf:',string_tfidf[i][1])
'''
#与上for循环等效
tfidf_list=[string_tfidf[i][1] for i in range(len(string_tfidf))]
print('tfidf_list:',tfidf_list)

'''

#以下代码为依据tfidf大小进行词语排序
import numpy as np
dtype=[('id',int),('score',float)]
values=np.array(string_tfidf,dtype=dtype) #string_tridf转为数组（方便设置名称），并设置每列的名称
values_sort=np.sort(values,order='score')#根据score列进行排序
print('sort:',values_sort)

values_sort_list=values_sort.tolist()#转为list是因为list可以使用reverse，进行降序排列
values_sort_list.reverse()
print('reverse list:',values_sort_list)

print(dictionary[values_sort_list[0][0]])#values_sort_list[0]表示最重要的词的元组，values_sort_list[0][0]表示最重要的词元组的id，dictionary[id]则是对应的词语

print("词语重要性排序：")
for i in range(len(values_sort_list)):
    print(dictionary[values_sort_list[i][0]])

























