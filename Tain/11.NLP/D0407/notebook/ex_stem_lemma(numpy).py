from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.tokenize import *
from nltk.tag import pos_tag
import string
from nltk.corpus import stopwords
import numpy as np
import re
import pandas as pd
landstem=LancasterStemmer()
stops=stopwords.words('english')    
lemmma=WordNetLemmatizer()    
with open('../DATA/test.txt') as f:
    text=f.read()
text=text.lower()
sent_list=sent_tokenize(text)
# ============================================
# word split
# 불용어처리
stop_dict=dict(zip(stops,['']*len(stops)))
sent_word_list=[]
for sent in sent_list:
    s=word_tokenize(sent)
    s=pd.Series(s).replace(stop_dict)
    s=s.tolist()
    new=[]
    for x in s:
        for punc in string.punctuation:
            x=x.replace(punc,'')
        if len(x)>1:
            new.append(x)
    lem=[lemmma.lemmatize(y[0],'a' if y[1][:2]=='JJ' else 'v' if y[1][:2]=='VB' else 'n') if y[1][:2] in ['JJ','VB'] else y[0] for y in pos_tag(new)]
    sent_word_list.append(lem)
# vocab
vocab=[y for x in sent_word_list for y in x]
vocab=np.unique(vocab).tolist()
vocab_dict={'<ukn>':1,'<pad>':0}
for x,y in enumerate(vocab,2):
    vocab_dict[y]=x
sent_num=[]
max=0
for idx,sent in enumerate(sent_word_list):
    len_list=len(sent)
    if max<len_list:
        max=len_list
for sent in sent_word_list:
    sent_num.append(pd.Series(sent).replace(vocab_dict).to_list()+[0]*(max-len(sent))) 
from torch.nn import Embedding