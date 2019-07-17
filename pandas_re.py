# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 07:11:29 2018

@author: YWZQ
"""
import pandas as pd
import numpy as np
import re
a = [['-', 'DDD', '+-'], ['3+', 'Ⅳ', '++++-'], ['Ⅳ度', '-        0mmol/L', '3']]
df = pd.DataFrame(a)
print(df)



def return_class(s):
    p5=r'\+{3,}|HP|hp|3\+'
    pattern5=re.compile(p5)
    p4=r'\+{2,}'
    pattern4=re.compile(p4)
    p3=r'\+|阳'
    pattern3=re.compile(p3)
    p2=r'\+\-'
    pattern2=re.compile(p2)
    p1=r'DDD'
    pattern1=re.compile(p1)
    
    
    if pattern1.findall(s):
        a=1
    elif pattern5.findall(s):
        a=5
    #if re.findall("\+{2,}",s):
     #   a=2
    elif pattern4.findall(s):
        a=4
    elif pattern2.findall(s):#注意，这里先检测2否则2会被3掩盖
        a=2
    elif pattern3.findall(s):
        a=3
   
    if pattern1.findall(s):
        a=666
    
    else:
        a=0
    return (a)



for i in df.columns:
    df[i]=df[i].map(return_class)
    #df[i]=df[i].map(lambda s:1 if(re.findall(r"\-",s))else 0)

         
'''
    for j in df[i].index:
        #df[i][j]=''.join(re.findall(r"\d+\.?\d*",df[i][j]))
        df[i][j]=(1 if(re.findall(r"瘤|明|病史|史",df[i][j]))else 0)
'''        
   
df.fillna(0,inplace=True)
df.replace('',0,inplace=True)

        
print(df)
#print(df_re)




