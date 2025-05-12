from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.tokenize import *
from nltk.tag import pos_tag
import string
from nltk.corpus import stopwords
landstem=LancasterStemmer()
# print(f'[working, worked, works] ', end='여간 추출 =>')
# print(landstem.stem('working'),landstem.stem('worked'),landstem.stem('works'))
stops=stopwords.words('english')    

lemmma=WordNetLemmatizer()
with open('../DATA/test.txt') as f:
    text=f.read()
text=text.lower()
sent_list=sent_tokenize(text)
word=[]
stops=stopwords.words('english') 
# 단어 사전 생성
# - 토큰: 정수 인코딩
# - 특수토큰: 없는 토큰 'unk', 길이 맞춤용 토큰:  'pad' 
for x in sent_list:
    x=[lemmma.lemmatize(y[0],'a' if pos_tag([y[0]])[0][1][:2]=='JJ' else 'v' if pos_tag([y[0]])[0][1][:2]=='VB' else 'n' ) if y[1][:2] in ['JJ','VB','NN'] else y[0] for y in pos_tag(word_tokenize(x))]
    word.extend(x)
word_list=[]
for x in word:
    for y in x:
        if y in string.punctuation:
            x=x.replace(y,'')
        else: x
    word_list.append(x) 
word=list(set(word_list))
word=[x for x in word if not x in string.punctuation]
for stop in stops:
    if stop in word:
        del word[word.index(stop)]
    else: pass
# =====================================================
vocab={'<pad>':0, '<UNK>':1}
for x,y in enumerate(word,2):
    vocab[y]=x
# tokenize
sent_token_list=[]
for x in sent_list:
    sent_token_list.append(word_tokenize(x))
# 불용어 처리
sent_new_list=[]
for sent in sent_token_list:
    sent_new=[]
    for stop in stops:
        count=0
        for text in sent: 
            if text==stop:
                count+=1
        for rep in range(count):
            del sent[sent.index(stop)]
    sent_new.append(sent)
    sent_new_list.extend(sent_new)
# 필요없는 puctuation 버리기 및 교체
sent_punc_list=[]
for sent in sent_new_list:
    sent1=[]
    for text in sent:
        for alpha in text:
            if alpha in string.punctuation:
                text=text.replace(alpha,'')
        if len(text)>1:
            sent1.append(text)
    sent_punc_list.append(sent1)
sent_new_list1=[]
for x in sent_punc_list:
    a=[lemmma.lemmatize(y[0],'a' if pos_tag([y[0]])[0][1][:2]=='JJ' else 'v' if pos_tag([y[0]])[0][1][:2]=='VB' else 'n' ) if y[1][:2] in ['JJ','VB','NN'] else y[0] for y in pos_tag(x)]
    sent_new_list1.append(a)
# ==================================================
# 정수타입으로 바꾸기
num_sent=[]
for x in sent_new_list1:
    num_=[]
    for y in x:
        num_.append(vocab[y])
    num_sent.append(num_)
print(num_sent)
            
            
        
    
