import torch.nn as nn
class Skipgram(nn.Module):
    def __init__(self,vocab_size,embedding_size):
        super().__init__()
        self.embedding=nn.Embedding(vocab_size,embedding_size)
        self.linear=nn.Linear(embedding_size,vocab_size)
    def forward(self,data):
        embedding=self.embedding(data)
        return self.linear(embedding)
import pandas as pd
from Korpora import Korpora
from konlpy.tag import Okt
import re
import string
corpus=Korpora.load('nsmc')
corpus=pd.DataFrame(corpus.test)
punc=dict(zip(string.punctuation, ['']*len(string.punctuation)))
corpus.text=corpus.text.str.replace(r"[!\"""#$%&'()*+,-./:;<=>?@[\]^_`{|}~]",'',regex=True)
tokenizer=Okt()
rgex=re.compile(r'^[가-힣]+')
tokens=[(tokenizer.morphs(y),x) for x,y in enumerate(corpus.text) if re.search(rgex,y)]
with open('../DATA/koreanStopword.txt') as f:
    stops=f.readlines()

stops=[x.replace('\n','') for x in stops]
for stop in  stops:
    corpus.text=corpus.text.apply(lambda x:x.translate(str.maketrans('','',stop)))
tokenizer=Okt()
rgex=re.compile(r'^[가-힣]+')
tokens=[(tokenizer.morphs(y),x) for x,y in enumerate(corpus.text) if re.search(rgex,y)]
idx=[y for x,y in tokens]
value=[x for x,y in tokens]
label=corpus.label.iloc[idx]
from collections import Counter
def bulid_vocab(corpus,n_vocab,special):
    count=Counter(y for x in corpus for y in x)
    vocab=special
    count=count.most_common(n_vocab)
    for x, y in count:
        vocab.append(x)
    return {x:y for x,y in enumerate(vocab)},{y:x for x,y in enumerate(vocab)}
id2s,s2id=bulid_vocab(value,5000,['<unk>'])
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
word_pair=get_word_pairs(value,windowsize=2)
def get_index_pair(word_pair,s2id):
    pairs=[]
    unk_idx=s2id['<unk>']
    for x,y in word_pair:
        center_idx=s2id.get(x,unk_idx)
        context_idx=s2id.get(y,unk_idx)
        pairs.append([center_idx,context_idx])
    return pairs
index_pairs=get_index_pair(word_pair,s2id)
import torch
from torch.utils.data import TensorDataset,DataLoader

index_pairs=torch.tensor(index_pairs)
center_index=index_pairs[:,0]
context_index=index_pairs[:,1]
dataset=TensorDataset(center_index,context_index)
dataloader=DataLoader(dataset,batch_size=32,shuffle=True)

from torch.optim.lr_scheduler import ReduceLROnPlateau
import torch.optim as optim
from torchmetrics import Accuracy
import torch.nn.functional as F

device='cuda' if torch.cuda.is_available() else 'cpu'
word2vec=Skipgram(len(s2id),128).to(device)
optimizer=optim.SGD(word2vec.parameters(),lr=0.01)
LR=ReduceLROnPlateau(optimizer,mode='min',patience=4)
accuarcy=Accuracy(task='multiclass',num_classes=len(s2id))
for epoch in range(10):
    loss_score=0
    num=0
    pred_list=[]
    target_list=[]
    for label,target in dataloader:
        optimizer.zero_grad()
        output=word2vec(label)
        loss=F.cross_entropy(output,target)
        loss_score+=loss
        num+=label.size(0)
        loss.backward()
        pred_list.extend(torch.argmax(output,dim=1).tolist())
        target_list.extend(target.tolist())
        optimizer.step()
    accur=accuarcy(torch.tensor(pred_list,dtype=torch.int64),torch.tensor(target_list,dtype=torch.int64))
    LR.step(loss)
    print(f'epoch: {epoch}')
    print(f'정확도: {accur},loss: {loss/num:3f}')