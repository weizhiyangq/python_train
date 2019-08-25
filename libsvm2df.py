# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 22:41:29 2019

@author: YWZQ
"""

import pandas as pd
from sklearn.datasets import dump_svmlight_file


df1 = pd.DataFrame()
df1['a']= [1,2,3]
df1['b'] = [1,1,2]
#print(df1)
df1.to_csv('test_libsvm1.csv',index=None)

df2= pd.DataFrame()
df2['c']=[1,2]
df2['d']=[3,3]
df2.to_csv('test_libsvm2.csv',index=None,header=None)
df_read1 = pd.read_csv('test_libsvm1.csv')
df_read2= pd.read_csv('test_libsvm2.csv',header=None)
df_read1.columns=range(0,len(df_read1.columns))
#print(df_read1)
#print(df_read2)
df_concat=pd.concat([df_read1,df_read2])
print(df_concat)

'''
df = pd.read_csv("data.txt")      # 第一个字段为target
y = df.target      # y为数据的label值
dummy = (df.iloc[:, 1:])
mat = dummy.as_matrix()
dump_svmlight_file(mat, y, 'svm_output.libsvm', zero_based=False)   
'''