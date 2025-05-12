from nltk.tokenize import *
import string
from nltk.corpus import stopwords
from nltk.tag import pos_tag
stop1=stopwords.words('korean')
print(f'STOP_WORDS 총 갯수: {len(stop1)}')
print(f'STOP_WORDS: {stop1[:10]}')