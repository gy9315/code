import torch
import torch.nn as nn
import torch.nn.functional as F
from gensim.models.word2vec import Word2Vec
import pandas as pd
class Embedded_Model():
    def __init__(self,data:pd.Series):
        self.data=data
    def stopword(self):
        self.data=self.data.replace(r'[!\"#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]','',regex=True,inplace=True)
    def word2vec(self):
        wordvec=Word2Vec(list(self.data.tolist()),vector_size=128,alpha=0.02,window=3,min_count=1,sg=1,epochs=100,max_final_vocab=None)
        wordvec.save('word2vec.model')
        # torch.save(torch.tensor([wordvec.wv[word] for word in wordvec.wv.index_to_key]),'word2vec.model')
        return wordvec