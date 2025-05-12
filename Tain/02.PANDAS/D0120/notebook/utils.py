''' 
FILENAME: utils.py
DESCRIPTION: DataFrame 속성 관련 함수
DATE: 2025.01.20.
HISTORY:    WRITER      DATE            DESC
            KANG        20205.01.20.     print_attribute()
'''
# 함수기능: 데이터프레임 속성 출력
# 함수이름: print_attribut()
# 매개변수: x(DF type)
import pandas as pd
def print_attribute(x:pd.DataFrame,xname:str):
    print(f'------[{xname}]-------')
    print(f'dtype: {x.dtypes}')    
    print(f'col: {x.columns}')
    print(f'idx: {x.index}')
    print(f'dim: {x.ndim}')
    print(f'shape: {x.shape}')
    print(f'values: \n{x.values}')