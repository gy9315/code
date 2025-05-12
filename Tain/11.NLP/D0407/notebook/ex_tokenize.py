from nltk.tokenize import *
import string
import re
text = 'The Matrix is everywhere its all around us, here even in this room. \
    You can see it out your window or on your television. \
    You feel it when you go to work, or go to church or pay your taxes.'
# 문장 단위 토큰화
reult=sent_tokenize(text)
for x,y in enumerate(reult):
    print(f'{x}: {y}')
