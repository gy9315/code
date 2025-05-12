from konlpy.tag import *
from konlpy.corpus import kolaw,kobill
LAW_FILE=kolaw.fileids()[0]
BILL_FILE=kobill.fileids()
kolaw=kolaw.open(LAW_FILE).read()
print(kolaw)
han=Hannanum()
kkma=Kkma()
okt=Okt()
komoran=Komoran()
