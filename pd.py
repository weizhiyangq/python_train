import pandas as pd

d={'1':[7,1,1,0],'2':[3,1,0,1],'3':[0,9,1,2]}
d_pd=pd.DataFrame(d)
print(d_pd)


me=d_pd['1'].median()
d_pd['1']=d_pd['1'].map(lambda x:0 if x<me else x )
columns_name=d_pd.columns.tolist()

rename=['tt'+i for i in columns_name]
d_pd.columns=rename

print(d_pd)
'''
import re
pat=re.compile(".*?([\u4E00-\u9FA5])")
def return_0(x):
    x=str(x)
    if pat.findall(x):
        x=0
    return x
d_pd['1']=d_pd['1'].map(return_0)
print(d_pd)
'''
