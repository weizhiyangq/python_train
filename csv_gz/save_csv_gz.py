# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:20:59 2019

@author: YWZQ
"""

import pandas as pd
'''
a = pd.DataFrame(columns=['a','b'])
a['a'] = [[1,3],[2,3],[3,3],[4,8]]
a['b'] =[2,2,2,2]
a.to_csv('a.csv.gz',compression='gzip',index=False)
a.to_hdf('a.hdf','w',index=False)
print(a.info())
print(a.iloc[0,0][1])

'''
a_read = pd.read_csv('a.csv.gz')
#print('a info:\n',a_read.info())
b = pd.read_hdf('a.hdf')
#print('b info:\n',b.info())
print(a_read)
print(a_read.iloc[0,0][0])  #可见，csv保存形式不会保留dataframe中的特定形式，如列表变为了字符串
print(b)
print(b.iloc[0,0][0])  #可见hdf形式可以保存dataframe中数据的格式，如列表，但hdf保存占内存比csv大
