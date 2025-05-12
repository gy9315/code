# [1]
## [1-1]
import pandas as pd
data=[['김나나',35,'과장'],['이민아',28,'대리'],['박정민',30,'대리']]
dataDF=pd.DataFrame(data)
dataDF.columns=['이름','나이','직급']
print(dataDF)
## [1-2]
dataDF.drop('이름',axis=1,inplace=True)
## [1-3]
dataDF1=dataDF.drop([1,2])
print(dataDF1)
# [2]
data = [ ['037730', '3R', 1510, 7.36], ["036360", "3SOFT", 1790, 1.65], ["005760", "ACTS", 1185, 1.28],
]
columns = ["종목코드", "종목명", "현재가", "등락률"]
## [2-1]
dataDF=pd.DataFrame(data)
dataDF.columns=columns
print(dataDF)
## [2-2]
dataDF1=dataDF.drop(['종목코드','현재가'],axis=1)
## [2-3]
b=len(dataDF.index)
dataDF1=dataDF.drop(b-1)
## [2-4]
index = ["037730", "036360", "005760"]
data = [["3R", "1510"], ["3SOFT", 1790], ["ACTS", 1185]]
columns = ["종목명", "현재가"]
dataDF=pd.DataFrame(data)
dataDF.columns=columns
dataDF.index=index
print(dataDF)
## [2-5]
dataDF1=dataDF.drop(dataDF.index[0])
print(dataDF1)
## [2-6]
dataDF.drop([dataDF.index[0],dataDF.index[-1]],inplace=True)
print(dataDF)
# [3]
## [3-1]
DATA_PATH=r'C:\Users\gy931\OneDrive\Desktop\KDP-7\02.PANDAS\DATA\fish.csv'
fishDF=pd.read_csv(DATA_PATH)
print(fishDF)
## [3-2]
DATA_PATH=r'C:\Users\gy931\OneDrive\Desktop\KDP-7\02.PANDAS\DATA\iris.csv'
irisDF=pd.read_csv(DATA_PATH)
print(irisDF)
# [4]
## [4-1]
## 속성, 기능(method)
## [4-2]
## 객체: 메모리에 저장되는 것의 추상적 개념
## 인스턴스: 클라스를 활용하여 메모리에 실제 저장된 각각의 데이터
## [4-3]
''' 
    클라스를 활용하여 메모리에 인스턴스가 저장될 때
    각각의 속성의 차이가 있기에 각각 저장을 하지만
    
    함수 또는 method는 동일하게 작동을 하기에
    여러번 메모리에 저장할 필요없이 한번만 저장을 한다 
    
    각 인스턴스들이 해당 함수를 참조하게 만들기 위하여
    self라는 변수를 만들었고,
    해당 변수에는 각 인스턴스의 주소가 
    시스템 내부적으로 입력되어 앞서 말한 기능을 
    수행할 수 있게 된다.

'''  
## [4-4]
'''모듈은 동일한 류의 패키지들이 집단을 이루어서 만들어진 것이다.'''
## [4-5]
''' 모듈과 패키지를 사용하기 위해서 import가 필요하다.
    문법(모듈, 패키지 불러오는 법)
    import 모듈
    import 모듈.패키지'''
## [4-6]
''' __name__은 현재 실행하는 페이지가 main인지 아닌지 확인하는 변수이다.
    즉, 패키지에서 실행된게 원래 파일인지 불러온것인지 확인
    하는 변수이다.
'''
## [4-7]
# conda install kdt
# pip install kdt