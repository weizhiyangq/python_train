
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
import numpy as np
text = """我是一条天狗呀！
    我把月来吞了，
    我把日来吞了，
    天狗把一切的星球来吞了，
    天狗把全宇宙来吞了。
    我便是我了！"""
sentences = text.split()
#print(sentences)
sentence_word = [list(jieba.cut(sentence)) for sentence in sentences]
document = [" ".join(sentence) for sentence in sentence_word]

print('document:\n',document)

#tfidf_model = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b').fit(document)#token_pattern删掉了一个\\w，就可以匹配一个字的词语了

tfidf_model = TfidfVectorizer(min_df=0,max_df=0.999,token_pattern=r"(?u)\b\w+\b").fit(document)

print('vocabulary:\n',tfidf_model.vocabulary_)
sparse_result = tfidf_model.transform(document)
dense_result = tfidf_model.transform(document).todense()
print('sparse result\n',sparse_result)
print(sparse_result.data)
print(sparse_result.indices)
print(dense_result)
featureName = tfidf_model.get_feature_names()
print('featurename:\n',featureName)  #其实就是tfidf_model.vocabulary_中的各个词组成的一个列表,且是按键号顺序的，不过除去了各个词的键（即对应的数号id）

str_result = tfidf_model.transform(['一条 天狗 天狗'])
str_result_dense = tfidf_model.transform(['一条 天狗 天狗','天狗全宇宙']).todense()
print(str_result)
print(str_result.data)
print(tfidf_model.vocabulary_)
voca = tfidf_model.vocabulary_
#voca_replace = dict([val,key] for key,val in tfidf_model.vocabulary_.items())
str_result_dense=np.array(str_result_dense)[0]
#print(voca_replace)

print(str_result_dense)
tfidf_list = np.array([str_result_dense[voca[i]] for i in '一条 天狗 天狗'.split()])
print(tfidf_list)
