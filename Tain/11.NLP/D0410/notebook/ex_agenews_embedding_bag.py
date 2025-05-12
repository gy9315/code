import torch 
import torch.nn as nn
from torchtext.datasets import AG_NEWS
import spacy
from nltk import *
import string
import pandas as pd
lemma=WordNetLemmatizer()
a=AG_NEWS(split='train')
sent=[]
target=[]
for x,y in a:
    sent.append(y)
sent_word=[]
punc=dict(zip(string.punctuation,['']*len(string.punctuation)))
for x in sent:
    word_list=pd.Series(word_tokenize(x)).replace(punc).tolist()
    word_list=[x for x in word_list if len(x)>1]
    word_list=[lemma.lemmatize(x[0], 'a' if x[1][:2]=='JJ' else 'v' if x[1][:2]=='VB' else 'n') if x[1][:2] in ['JJ','VB'] else x[0] for x in pos_tag(word_list)]
    sent_word.append(word_list)
    