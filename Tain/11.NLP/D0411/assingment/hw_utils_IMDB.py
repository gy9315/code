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
print(torchtext.__version__)
EPOCH=30
DEVICE= 'cuda' if torch.cuda.is_available() else 'cpu'
# ==========================================================================================================================
# MODEL
class DNNModel(nn.Module):
    def __init__(self,word_vector):
        super().__init__()
        self.embeding=nn.EmbeddingBag.from_pretrained(word_vector,freeze=False,mode='mean',padding_idx=0)
        self.layer=nn.Sequential(nn.Linear(128,256),
        nn.BatchNorm1d(256),
        nn.ReLU(),
        nn.Linear(256,128),
        nn.Dropout(0.3),
        nn.BatchNorm1d(128),
        nn.ReLU(),
        nn.Linear(128,64),
        nn.BatchNorm1d(64),
        nn.ReLU(),
        nn.Linear(64,2))

    def forward(self,data,offset):
        out=self.embeding(data,offset)
        return self.layer(out)
    
class RNNModel(nn.Module):
    def __init__(self,word_vector):
        super().__init__()
        global DEVICE
        self.embeding=nn.Embedding.from_pretrained(word_vector,freeze=False,padding_idx=0)
        self.rnn=nn.RNN(128,128,3,batch_first=True,dropout=0.3,device=DEVICE)
        self.layer=nn.Linear(128,2)
        
    def forward(self,data):
        x=self.embeding(data).to(DEVICE)
        output,hd=self.rnn(x)
        out=self.layer(hd[-1])
        return out

class LSTModel(nn.Module):
    def __init__(self,word_vector):
        super().__init__()
        global DEVICE
        self.embeding=nn.Embedding.from_pretrained(word_vector,freeze=False,padding_idx=0)
        self.LSTM=nn.LSTM(128,128,3,batch_first=True,dropout=0.3,device=DEVICE)
        self.layer=nn.Linear(128,2)
        
    def forward(self,data):
        x=self.embeding(data).to(DEVICE)
        output,(hd,cell_state)=self.LSTM(x)
        out=self.layer(hd[-1])
        return out
        
# ==========================================================================================================================
# embedding
class Embedded_Model():
    def __init__(self,data:pd.Series):
        global DEVICE
        self.data=data
        nlp=spacy.load('en_core_web_sm')
        def get_lemma(text):
           doc=nlp(text)
           return [token.lemma_ for token in doc if not token.is_punct and not token.is_space]
        self.data=self.data.apply(get_lemma) 
            
    def custom_embed(self):
        class Skipgram(nn.Module):
            def __init__(self,vocab_size,embedding_size):
                super().__init__()
                self.embedding=nn.Embedding(vocab_size,embedding_size)
                self.linear=nn.Linear(embedding_size,vocab_size)
            def forward(self,data):
                embedding=self.embedding(data)
                return self.linear(embedding)

        def bulid_vocab(corpus,n_vocab,special):
            count=Counter(y for x in corpus for y in x)
            vocab=special
            count=count.most_common(n_vocab)
            for x, y in count:
                vocab.append(x)
            return {x:y for x,y in enumerate(vocab)},{y:x for x,y in enumerate(vocab)}
        def get_word_pairs(tokens,windowsize):
            pair=[]
            for sentence in tokens:
                sent_len=len(sentence)
                for idx,center_word in enumerate(sentence):
                    window_start=max(0,idx-windowsize)
                    window_end=min(sent_len,idx+windowsize+1)
                    center_word=sentence[idx]
                    context_word=sentence[window_start:idx]+sentence[idx+1:window_end]
                    for context in context_word:
                        pair.append([center_word,context])
            return pair
        def get_index_pair(word_pair,s2id):
            pairs=[]
            unk_idx=s2id['<unk>']
            for x,y in word_pair:
                center_idx=s2id.get(x,unk_idx)
                context_idx=s2id.get(y,unk_idx)
                pairs.append([center_idx,context_idx])
            return pairs
        self.id2s,self.s2id=bulid_vocab(self.data.tolist(),5000,['<unk>'])
        self.word_pair=get_word_pairs(self.data.tolist(),windowsize=2)
        self.index_pairs=get_index_pair(self.word_pair,self.s2id)
        index_pairs=torch.tensor(self.index_pairs)
        center_index=index_pairs[:,0]
        context_index=index_pairs[:,1]
        # ===================================================================
        dataset=TensorDataset(center_index,context_index)
        dataloader=DataLoader(dataset,batch_size=32,shuffle=True)
        custom=Skipgram(len(self.s2id),128).to(DEVICE)
        optimizer=optim.SGD(custom.parameters(),lr=0.001)
        LR=ReduceLROnPlateau(optimizer,mode='min',patience=10)
        for epoch in range(100):
            loss_score=0
            num=0
            pred_list=[]
            target_list=[]
            for label,target in dataloader:
                label,target=label.to(DEVICE),target.to(DEVICE)
                optimizer.zero_grad()
                output=custom(label)
                loss=F.cross_entropy(output,target)
                loss_score+=loss.item()
                num+=label.size(0)
                loss.backward()
                pred_list.extend(torch.argmax(output,dim=1).tolist())
                target_list.extend(target.tolist())
                optimizer.step()
            LR.step(loss_score)
            if LR.num_bad_epochs >= LR.patience:
                print('Early Stopping')
                torch.save(custom.embedding.weight.data.detach().cpu(),'custom.pkl') 
                break
    def word2vec(self):
        wordvec=Word2Vec(list(self.data.tolist()),vector_size=128,alpha=0.02,window=2,min_count=1,sg=1,epochs=100,max_final_vocab=5000)
        torch.save(torch.tensor([wordvec.wv[word] for word in wordvec.wv.index_to_key]),'word2vec.pkl')
        return {y:x for x,y in enumerate(wordvec.wv.index_to_key)}
# ==========================================================================================================================

def collate_batch_offset(batch,vocab):
    label_list, target_list, offsets = [], [], [0]
    for label, target in batch:
        label_list.append(vocab[label])
        processed_news = torch.tensor(target, dtype=torch.int64)
        target_list.append(processed_news)
        offsets.append(processed_news.size(0))
    label_list = torch.tensor(label_list, dtype=torch.float64)
    offsets = torch.tensor(offsets[:-1]).cumsum(dim=0)
    target_list = torch.cat(target_list)
    return label_list.to(DEVICE), target_list.to(DEVICE), offsets.to(DEVICE)

def collate_batch(batch,vocab):
    label_list, target_list= [], []
    for label,target in batch:
         label_list.append(vocab[label])
         processed_text = torch.tensor(target, dtype=torch.int64)
         target_list.append(processed_text)
    label_list = torch.tensor(label_list, dtype=torch.float64)
    target_list = pad_sequence(target_list, batch_first=True, padding_value=0)
    return label_list.to(DEVICE), target_list.to(DEVICE)
        

        
# ==========================================================================================================================
# DATASET
class CustomDataset(Dataset):
    def __init__(self,feature,target,mode=None):
        super().__init__()
        self.feature=feature
        self.target=target
        self.mode=mode
        if mode!=None:
            self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.feature,self.target,stratify=self.target)
    def __len__(self):
        if self.mode=='train':
            return self.x_train.shape[0]       
        if self.mode=='test':
            return self.x_test.shape[0] 
        if self.mode==None:
            return self.feature.shape[0] 
    def __getitem__(self, index):
        if self.mode=='train':
            return self.x_train.iloc[index,:], self.y_train.iloc[index]         
        if self.mode=='test':
            return self.x_test.iloc[index,:], self.y_test.iloc[index]     
        if self.mode==None:
            return self.feature.iloc[index,:], self.target.iloc[index]
    
# ==========================================================================================================================
# function
def normal_train(model_class,word_vecotor,feature,target,collate_fn):
    model=model_class(word_vecotor)
    optimizer=optim.Adam(model.parameters(),lr=0.001)
    LR=ReduceLROnPlateau(optimizer=optimizer,mode='min',patience=10)
    train_dataset=CustomDataset(feature,target,'train')
    test_dataset=CustomDataset(feature,target,'test')
    train_loader=DataLoader(train_dataset,batch_size=40,collate_fn=collate_fn)
    test_lodaer=DataLoader(test_dataset,batch_size=40,collate_fn=collate_fn)
    accur=Accuracy(task='multiclass',num_classes=2)
    for epoch in range(EPOCH):
        loss_list=[]
        total_loss=0
        pred_=[]
        fact_=[]
        model.train()
        model.to(DEVICE)
        for x, y in train_loader:
            x,y=x.to(DEVICE),y.to(DEVICE)
            y=y.view(-1)
            optimizer.zero_grad()
            output=model(x)
            loss=F.cross_entropy(output,y) 
            total_loss+=loss.item()
            loss.backward()
            optimizer.step()
            pred_train=torch.argmax(output,dim=1).tolist()
            pred_.extend(pred_train)
            fact_.extend(y.tolist())
        score=accur(torch.tensor(pred_) ,torch.tensor(fact_))
        print(f'epoch: {epoch}')
        print(f'[train] score: {score}, total loss: {total_loss}')
        model.eval()
        loss_list=[]
        total_loss=0
        pred_=[]
        fact_=[]
        with torch.no_grad():
            for x,y  in test_lodaer:
                x,y=x.to(DEVICE),y.to(DEVICE)
                y=y.view(-1)
                output=model(x)
                loss=F.cross_entropy(output,y) 
                total_loss+=loss.item()
                pred_train=torch.argmax(output,dim=1).tolist()
                pred_.extend(pred_train)
                fact_.extend(y.tolist())
        score=accur(torch.tensor(pred_) ,torch.tensor(fact_))
        print(f'epoch: {epoch}')
        print(f'[test] score: {score}, total loss: {total_loss}')
        LR.step(total_loss)