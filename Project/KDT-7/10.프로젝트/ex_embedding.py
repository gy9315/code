from utils import *
# ==============================
# 데이터 변환
DF=pd.read_csv('./DATA/age.csv')
age=DF['나이'].unique().tolist()
encode=[6,4,2,7,3,5,1,0]
age2int=dict(zip(age,encode))
int2agee=dict(zip(age,encode))
target=DF['나이'].replace(age2int)
print(target)