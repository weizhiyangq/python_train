# -*- coding: utf-8 -*-
"""
Created on Sat Dec 1 09:27:34 2018

@author: YWZQ
"""


'''
import os
print(os.listdir("text_page_1"))
first_list=os.listdir("text_page_1")
first_wether_text=[os.path.isfile("text_page_1/"+i) for i in first_list]
print(first_wether_text)
first_text_index=[i for i,x in enumerate(first_wether_text) if x==True]
print(first_text_index)
first_text=[]
first_text=list([first_list[i] for i in first_text_index])
print(first_text)
for i in first_text:
    first_list.remove(i)
print(first_list)
'''
import os
class Solution(object):
    def dir_combine(self,now_dir):
        def dfs(self,now_dir,res):
            if os.path.isfile(now_dir):
                return res.append(now_dir)
            for i in os.listdir(now_dir):
                i=now_dir+"/"+i
                dfs(self,i,res)
        res=[]
        dfs(self,now_dir,res)
        return res
if __name__=="__main__":
    res=Solution().dir_combine("text_page_1")
    print(res)
    print(len(res))
    
'''  
#也可以这样操作，不过后续还要进行一些处理，不一定简单
import os
walk = os.walk('text_page_1')
print(list(walk))
'''