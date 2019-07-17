# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:26:58 2018

@author: YWZQ
"""

'''
#例1
# coding:utf-8
# 引入 word2vec
from gensim.models import word2vec

# 引入日志配置
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 引入数据集
raw_sentences = ["the quick brown fox jumps back home  over the lazy dogs go home dd back home","yoyoyo you and he go home now to sleep back home"]

# 切分词汇
sentences= [s.split() for s in raw_sentences]
print(sentences)

# 构建模型
model = word2vec.Word2Vec(sentences, min_count=1)

# 进行相关性比较
print('similarity between go and home:',model.similarity('go','home'))
'''
raw_corpus = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",              
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

stoplist = set('for a of the and to in'.split(' '))
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in raw_corpus]

from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

precessed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
for i in precessed_corpus:
    print(i)     #显示每个文档，即每行，单词在所有文档累计个数超过1的单词
    


from gensim import corpora
dictionary = corpora.Dictionary(precessed_corpus)#为得到的单词表进行唯一性操作，得到无重复的单词字典
print(dictionary)
for i in dictionary:
    print(i,dictionary[i])
print(dictionary.token2id)#无重复的单词及对应id
new_doc = "human computer interaction"#准备检测用的文档
new_vec = dictionary.doc2bow(new_doc.lower().split())
print (new_vec) #显示检测文档单词id及个数，id对应在上述语料库得到的个数超过1的单词id，若检测文档的单词未在id表中出现，则不显示
bow_corpus = [dictionary.doc2bow(text) for text in precessed_corpus]

print(bow_corpus)


#显示权重
from gensim import models
tfidf = models.TfidfModel(bow_corpus)
string = "system minors graph graph human"
string_bow = dictionary.doc2bow(string.lower().split())#得到system和minors的id和个数
string_tfidf = tfidf[string_bow]#由于system在上面的语料库中出现4次，而minors2次，说明system是更常见的词，所以重要性小，但是，如果将system在需检测的文档中的出现次数提高，也可将他的重要性提高
print (string_bow)  
print (string_tfidf)

for i in range(len(string_tfidf)):
    print(string_tfidf[i][1])

tfidf_list=[string_tfidf[i][1] for i in range(len(string_tfidf))]

print(tfidf_list)


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