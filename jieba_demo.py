# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 09:01:30 2018

@author: YWZQ
"""
'''
#最简单用法
import jieba

seg_list=jieba.cut("我来到华南农业大学",cut_all=True,HMM=False)
print("full mode:",','.join(seg_list))
seg_list=jieba.cut("我来到华南农业大学",cut_all=True,HMM=True)
print("full mode:",'/'.join(seg_list))
seg_list=jieba.cut("我来到华南农业大学",cut_all=False)
print("default mode",'/'.join(seg_list))
seg_list=jieba.cut_for_search("我来到华南农业大学")
print('/'.join((seg_list)))

'''


'''
#读写文件与结巴，并且自建划分词
import jieba
jieba.load_userdict('结巴自写词典.txt')#把想划分的词放在此文件里，然后会自动使用


#jieba.add_word('红海行动')  #直接增加划分词,和load_userdict效果差不多
#jieba.add_word('看了')
#jieba.del_word('看了') #删除划分词
#jieba.del_word('红海行动')


with open(u'分词前评论.txt') as f:  #读取原始文本，默认为‘r’，也可标注
    lines=f.readlines()
   
    for line in lines:
        print(line)
        seg_list=jieba.cut(line,cut_all=False)
        seg_list='/'.join(seg_list)
        print(seg_list)
        with open('E:\pythonlianxi\分词后.txt','a') as file_object:  #‘a’和‘w’的区别是，‘w’会覆盖原来文本，‘b’是增添
            file_object.write(seg_list)
    
    #line=f.readline()
print('end')
'''



'''
#功能是实现关键词提取
#注意，结巴并行处理不能再window下进行
import jieba
import jieba.analyse
#jieba.enable_parallel(3)
with open(r'E:\pythonlianxi\jiebaxiaoshuo.txt',encoding='UTF-8') as f:
    lines=f.readlines()
    for line in lines:
        seg_list=jieba.cut(line,cut_all=False)
        seg_list='/'.join(seg_list)
        with open(r'E:\pythonlianxi\duancixiaoshuo.txt','a',encoding='UTF-8') as f2:
            f2.write(seg_list)
        str1=''.join(seg_list)
    str1=''.join(lines)
    tags = jieba.analyse.extract_tags(str1,topK=100) #指定提取100个词作为关键词
    
    

print(','.join(tags))
print('end')

'''

'''
#显示词性
import jieba
import jieba.posseg as psg
message='他很满足，因为只要庄稼在，就代表他们一家人有吃不完的粮食，而让他更满足的，则是他每次看到自己的儿子时'
words=psg.cut(message)
for word,flag in words:
    print('%s %s'%(word,flag))
'''


import jieba.analyse

message='尽管他们看不到他，可孟浩还是跪在那里，磕了一个头，目中露出柔和，那双眼内蕴含了曾经无数年的追忆，那曾经的一幕幕画面，在孟浩的脑海里清晰的浮现，妖仙古宗认柯父的情感，那种首次体会到父爱的感情，在这一瞬，于孟浩心中不断地沉淀下来。'

jieba.analyse.set_stop_words('E:\pythonlianxi\jiebastopword.txt')

tags=jieba.analyse.extract_tags(message)#提取关键词

print(','.join(tags))












   