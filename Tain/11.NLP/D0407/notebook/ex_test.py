from nltk.tokenize import *
import string
import re
txt="Happy,New Year! Don't stop"
punc=string.punctuation
for x in txt:
    if x in punc:
        txt=txt.replace(x,'')
# print(txt)
txt1=txt.lower()
result=word_tokenize(txt1)
del result[result.index('dont')]
# print(result)
result1=wordpunct_tokenize(txt)
print(result1)

a=[1,2,3,4]
if 1 in a:
    del a[a.index(1)]
print(a)
