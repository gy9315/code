import spacy
from konlpy.corpus  import kobill,kolaw
import string
import spacy.parts_of_speech as pos
LAW_FILE=kolaw.fileids()[0]
KO_MODEL='ko_core_news_sm'
LAW_CORPUS=kolaw.open(LAW_FILE).readlines()
# LAW_CORPUS=[y.strip() for y in LAW_CORPUS if y.strip()!='']
for x,y in enumerate(LAW_CORPUS):
    if len(y.strip())==0:
        del LAW_CORPUS[x]
    else: 
        for punc in string.punctuation:
            y=y.replace(punc,'').strip()
            y=y.replace('\n','')
        LAW_CORPUS[x]=y
# for x, y in enumerate(LAW_CORPUS):
#     print(x,y)
# =============================================================================================
word_total_list=[]
for x in LAW_CORPUS[:2]:
    model=spacy.load(KO_MODEL)
    model.Defaults.stop_words.update(['을,를'])
    doc=model(x)
    word_f_list=[]
    for token in doc:
        lam=token.lemma_.split('+')
        tag=token.tag_.split('+')
        word_list=list(zip(lam,tag))
        # print(word_list)
        for idx,(x,y) in enumerate(word_list):
            # print(y[0])
            if y[0].strip() in ['j','s','_']:
                del word_list[idx]
        if len(word_list) !=0:
            word_f_list.extend(word_list)
        else: pass
    word_total_list.append(word_f_list)
# print(word_total_list)
for x in word_total_list:
    print(x)
    print([y[0] for y in x])
    print('*'*10)

        
        
        

