# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:37:32 2019

@author: YWZQ
"""

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

docs = ['$#%^2fw fsdddg^&@ fsdddg^&@ fsgs7 *&$hfh','dfs@#$ df45 fsdddg^&@ fgs%','fgs bh7 gh &^%']
vectorizer = TfidfVectorizer(token_pattern=r'\S+')
X = vectorizer.fit_transform(docs)
terms = vectorizer.get_feature_names()

print(terms)
print(X)
print(X.todense())
print('test:\n')
print(vectorizer.transform(['fsdddg^&@  *&$hfh']).todense())

n_topics = 2
lsa = TruncatedSVD(n_topics)
x2 = lsa.fit_transform(X)
print(x2)
print(lsa.components_)  #shape:[n_topics,word]

#from collections import defaultdict
#term_lsa = defaultdict(list)
term_lsa = {}
position = 0
for i in terms:
    term_lsa[i] = lsa.components_[:,position] 
print(term_lsa)  
