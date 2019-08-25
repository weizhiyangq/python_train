# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:49:15 2019

@author: YWZQ
"""

import joblib
from joblib import Parallel, delayed
from math import sqrt


list_list = [[1,2,3,4],[-1,3,2,1],[-9,3,-1,-4]]
count = 0
def my_fun(l):
    global count
    for i in l:
        if i>0:
            count+=1

Parallel(n_jobs=2)(delayed(my_fun)(l) for l in list_list)
print(count)

'''
def fun(dic):
    
'''   