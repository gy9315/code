from nltk.tokenize import *
import string
from nltk.tag import pos_tag
from nltk.corpus import stopwords
# 자연어 전처리 - 정제+토근화
PATH='../DATA/test.txt'
STOP_WORD=''
with open(PATH,'r') as f:
    data=f.read()
# 대소문자 일치
data=data.lower()
print(len([x for x in data if x.isupper()]))
# =======================================================================
punc=string.punctuation
data=sent_tokenize(data)

data_list=[]
for x in data:
    for y in punc:
        if y in x:
            x=x.replace(y,'') 
    data_list.append(x)
word_list=[]
for x in data_list:
    word=wordpunct_tokenize(x)
    word_list.extend(word)
word=set(word_list)
word_list=pos_tag(word)
dict1={y:[x] for x,y in word_list}
c=[dict1[y].append(a) for a,b in word_list for y in dict1.keys() if b==y]
word={x:list(set(dict1[x])) for x in dict1.keys()}
# =======================================================================
stop1=stopwords.words('english')
word_list=[]
for x in word.values():
    for y in stop1:
        if y in x:
            del x[x.index(y)]
        else: pass
word={x: word[x] for x in word.keys() if len(word[x]) !=0}
print(word)
        