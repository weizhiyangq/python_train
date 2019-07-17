import pandas as pd
import numpy as np
import re
a = [['+', '++', '+-'], ['-+', '+++', '++++-'], ['阴', '5', '1']]
df = pd.DataFrame(a)
dict={}
for i in df.iloc[:,1]:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
    
