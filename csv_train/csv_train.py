# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:28:45 2019

@author: YWZQ
"""

import csv
import numpy as np
csv_file = csv.reader(open('testa.csv'))
#print(list(csv_file))
#print(np.array(list(csv_file)))
for i in range(10):
    a = next(csv_file)
    print(a)

b=[1,2,3]
b_filter = filter(lambda x:x,b)
print(list(b_filter))