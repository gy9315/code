# DataFrame 생성하기: 표만들기
# DataFrame 생성하기: 표만들기
import pandas as pd
# 전역변수 
data={'홍':[17,'남','덕영고'],'마':[15,'여','대구중']}
# DataFrame 만들기
# dict 타입의 데이터
# - key가 컬럼식별자로 설정
# - value가 컬럼값으로 설정
# - 예)      홍    마
#       0    17   15
#       1    남    여
#       2   덕영고  대구중
dataDF=pd.DataFrame(data,index=['나이','성별','학교'])
print(dataDF)