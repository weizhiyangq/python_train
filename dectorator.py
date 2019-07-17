# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:02:26 2018

@author: YWZQ
"""

def pri(*args,**kwargs):
    print(args[2])
    print(kwargs)

a=1
b=2
c=3
pri(a,b,c)