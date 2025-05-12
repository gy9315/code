from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd

# ==============================================================================
# 
#
#    Make_word_Text.py 에서 만들어진 텍스트 을 불러오세요.txt
#
#
#=================================================================================
text = open('./방산_우대사항.txt',encoding='utf-8').read() #텍스트 파일 넣기 (신버전 우대사항내용찾기 이용 바람)
okt=Okt()

okt_morphs = okt.nouns(text)                       # (1) 형태를 결정해야함 ex: 명사, 형용사 등 

#====================================================================================
#
#   제외할 단어들을 설정해주세요~!!      
# 
#====================================================================================
stopwords = {'우대', '및', '등', '분','경력','신분','업무','설계','자격','방산','방산','위','보유','보유'
             '채용','가능','요건','마감','유','이력서','학과','이상','사용','사용','모집'
             '업무','근무','사항','관련','개발','경험'} # (2)불용어 결정 + 딕셔너리가 처리 속도가 더 빠름
filtered_words = [word for word in okt_morphs if word not in stopwords]

#=========================================================================================
# csv 만들기 용 데이터 프레임 만들기
word_counts = Counter(filtered_words)

df = pd.DataFrame(word_counts.items(), columns=['단어', '빈도'])
df = df.sort_values(by='빈도', ascending=False).reset_index(drop=True)



# CSV 파일로 저장 (UTF-8 인코딩)
#df.to_csv(file, encoding='utf-8-sig')

#=========================================================================================
#
# 워드클라우드 만들 이미지 파일 
#   원하는 이미지 파일 위치 넣기
#
img_mask = np.array(Image.open('./DATA/image/사람1.png'))
#=========================================================================================

wordcloud = WordCloud(
    font_path='malgun.ttf',  
    background_color='white',
    width=800,
    height=400,
    mask=img_mask
).generate_from_frequencies(word_counts)

# 워드클라우드 표시
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show() 