import pandas as pd
import torch
import torch.nn as nn
import torch.utils
from torch.utils.data import TensorDataset, DataLoader,Dataset
from sklearn.model_selection import train_test_split
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import ReduceLROnPlateau
import numpy as np
from torchmetrics.classification import Accuracy     
from gensim.models.word2vec import Word2Vec
import string
import spacy
import torchtext
from collections import Counter
from torch.nn.utils.rnn import pad_sequence
import pickle


DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
## 클래스이름 : TextModelComplex
## 부모클래스 : Module
## 매개변수   : 단어사전 갯수(vocab_size), 임베딩 차원(embed_dim),
##              중간 은닉층 차원(hidden_dim), 분류 클래스 갯수(num_class),
##              드롭아웃 확률(dropout_p)
## -------------------------------------------------------------------------
class LSTModel(nn.Module):
    def __init__(self,word_vector):
        super().__init__()
        global DEVICE
        self.embeding=nn.Embedding.from_pretrained(word_vector,freeze=False,padding_idx=0)
        self.LSTM=nn.LSTM(256,128,3,batch_first=True,dropout=0.2,device=DEVICE,bidirectional=True)
        self.layer=nn.Sequential(
            nn.Linear(512,128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout1d(0.1),
            nn.Linear(128,64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout1d(0.1),
            nn.Linear(64,32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Linear(32,8))
        
    def forward(self,data):
        x=self.embeding(data).to(DEVICE)
        output,(hd,cell_state)=self.LSTM(x)
        print(hd.size())
        # hd=hd.unsqueeze(0)
        # if hd.shape[0] >= 2:
        hd=torch.cat([hd[-2], hd[-1]], dim=1)
        # else:
        #     hd=hd[-1]
        # hd=hd.unsqueeze(0)
        avg_emb=x.mean(dim=1)
        print(hd.size())
        hd=torch.cat([hd,avg_emb], dim=1)
        out=self.layer(hd)
        return out
    
def embed(data,vocab):
    data=pd.DataFrame([data],columns=['대사'])
    data['대사'].replace(r'[!\"#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]','',regex=True,inplace=True)
    nlp=spacy.load('ko_core_news_sm')
    def get_lemma(text):
        doc=nlp(text)
        return [token for token in doc if not token.is_punct and not token.is_space]
    data=data['대사'].apply(get_lemma) 
    stopword='은는을를에'
    sent=[]
    for x in data.tolist():
        small=[]
        for y in x:
            small.append(str(y).translate(str.maketrans('','',stopword)))
        sent.append([x for x in small if len(x)!=0])
    data=pd.Series(sent)
    label=torch.LongTensor([vocab.get(x,vocab['<ukn>']) for x in data.item()])
    return label.to(DEVICE).unsqueeze(0)
        
def test(model_class,model_path,word_vecotor,data,vocab):
    model=model_class(word_vecotor).to(DEVICE)
    model.load_state_dict(torch.load(model_path,weights_only=True,map_location=torch.device('cpu')))
    model.eval()
    # =============================================================================================
    x=embed(data,vocab)
    with torch.no_grad():
        x=x.to(DEVICE)
        output=model(x)
        pred=torch.argmax(output,dim=1).item()
        prob=round(F.softmax(output,dim=1).max(dim=1).values.tolist()[0]*100,2)
    int2w={y:x for x,y in {'60대': 6, '40대': 4, '20대': 2, '70대': 7, '30대': 3, '50대': 5, '10대': 1, '아동': 0}.items()}
    return int2w[pred], prob
        
vocab=torch.load('../vocab.pkl')
word2vec=torch.load('../word2vec.pkl')
a=torch.zeros(1,word2vec.size(1))
b=torch.randn(1,word2vec.size(1))*0.01
word2vec=torch.cat([a,b,word2vec],dim=0)