import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder,LabelEncoder,StandardScaler,MinMaxScaler
import torch.nn as nn
from utils import *
from torchmetrics import R2Score 
from torch.optim.lr_scheduler import ReduceLROnPlateau
DF=pd.read_csv('../DATA/taxis.csv')
# print(DF)

# ====================================
# 야간 할증, 러시아워 할증, 공항할증
# cash는 tip 책정불가, credit 책정 / 요금대비 %지불
# 택시 탑승 시간대 별 분류 
# 탑승 시간 컬럼 추가
# 시와 시를 이동한경우 1,0이진화, 
# 요금 + 톨비 합친 값이 target 데이터
# 탑승 장소 두개의 데이터를 one-hot encoder 
# ===================================
# 데이터 시간-> 시간 데이터로 변경 -> 탑승시간대 변경 -> 걸린시간 컬럼추가
# 
# passenger drop
# color drop
# total drop
# distance가 0인거 제거: 미터기 끄고 계산진행한거거
# fare+tolls 합치기
# ====================================
# 최종목표: 탑승시간, 출발지, 도착지 -> 요금
# 1. 탑승시간, 출발지, 도착지 -> 소요시간, distance
# 2. 탑승시간, 소요시간, distance, 시이동(O/X), 지불방법 -> 요금
# ====================================
# [1] 시간데이터 변경
DF['pickup']=pd.to_datetime(DF['pickup'],format='%Y-%m-%d %H:%M:%S')
DF['dropoff']=pd.to_datetime(DF['dropoff'],format='%Y-%m-%d %H:%M:%S')
DF.drop(['color','total','passengers'],axis=1,inplace=True)
# ===================================
# 결측치 처리
DF.loc[(DF['tip']==False) & (DF['payment'].isna()),'payment']='cash'
idx=DF[DF['distance']==0].index
DF.drop(index=idx,inplace=True)
# pickup_zone 등 object==nan 전부 drop
DF.dropna(axis=0,how='any',inplace=True)
# ===================================
# label 숫자로 변경
label=[['pickup_zone','pickup_borough'],['dropoff_zone','dropoff_borough']]
# borough와 zone을 합치기
# 맨 앞에 borough 인코딩, 이후 원핫인코드

onelabel=[]
for x in label:
    en=OneHotEncoder(sparse_output=False)
    en1=en.fit_transform(DF[[x[1]]].values)
    en=OneHotEncoder(sparse_output=False,drop='first')
    en2=np.hstack((en1,DF[[x[0]]].values))
    en3=en.fit_transform(en2)
    onelabel.append((en3))
pickup_DF=pd.DataFrame(onelabel[0])
dropoff_DF=pd.DataFrame(onelabel[1])
dropoff_DF.columns=range(195,195+len(dropoff_DF.columns))
taketimeDF=DF['dropoff']-DF['pickup']
taketimeDF=taketimeDF.dt.total_seconds()/60
taketimeDF=taketimeDF.apply(lambda x: round(x,2))
taketimeDF=taketimeDF.to_frame()
taketimeDF.columns=['time']
DF.loc[:,'pickup']=DF['pickup'].dt.hour.copy()
DF.loc[:,'dropoff']=DF['dropoff'].dt.hour.copy()
DF.loc[:,'payment']=DF['payment'].map({'credit card':1,'cash':0})
zoneDF=pd.concat([pickup_DF,dropoff_DF],axis=1)
DF.reset_index(drop=True,inplace=True)
taketimeDF.reset_index(drop=True,inplace=True)
a=pd.concat([DF.loc[:,:'payment'],taketimeDF,zoneDF],axis=1)
# ========================================================
# 1. 탑승시간, 출발지, 도착지 -> 소요시간, distance
# 출발지 range(0,195), 도착지 range(195,402)
feature_list=[]
feature_list.extend(range(0,402))
target_list=['distance']
scale=StandardScaler()
scale_target=StandardScaler()
featureDF=a.loc[:,feature_list]
featureDF=scale.fit_transform(featureDF.values)
# print(featureDF.shape)
targetDF=a.loc[:,target_list]
targetDF=scale_target.fit_transform(targetDF)
class DistanceModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.feature1=nn.Linear(195,32)
        self.feature2=nn.Linear(207,32)
        self.outlayer=nn.Sequential(
            nn.SiLU(),
            nn.Linear(32,64),
            nn.Dropout(0.1),
            # nn.BatchNorm1d(64),
            nn.SiLU(),
            nn.Linear(64,32),
            nn.Dropout(0.1),
            # nn.BatchNorm1d(32),
            nn.SiLU(),
            nn.Linear(32,1)
        )
    def forward(self,feature1,feature2):
        feature1=self.feature1(feature1)
        feature2=self.feature2(feature2)
        interaction=torch.abs(feature2 - feature1)
        return self.outlayer(interaction)
    
train_dataset=MyDataset(featureDF,targetDF,mode='train')
test_dataset=MyDataset(featureDF,targetDF,mode='test')
train_loader=DataLoader(train_dataset,batch_size=45)
test_loader=DataLoader(test_dataset,batch_size=45)
model=DistanceModel()
score=R2Score()
optimizer=optim.Adam(model.parameters(),lr=0.001)
Lr=ReduceLROnPlateau(optimizer=optimizer,patience=5,mode='min')
for epoch in range(300):
    model.train()
    device='cuda' if torch.cuda.is_available() else 'cpu'
    model.to(device)
    pred_=torch.Tensor()
    fact_=torch.Tensor()
    total_loss=0
    for x,y in train_loader:
        x,y=x.to(device),y.to(dtype=torch.float32,device=device)
        optimizer.zero_grad()
        output=model(x[:,:195],x[:,195:])
        loss=F.mse_loss(output,y)        
        loss.backward()
        optimizer.step()
        total_loss+=loss.item()
        pred_=torch.hstack((pred_,output.squeeze()))
        fact_=torch.hstack((fact_,y.squeeze()))
    pred_=scale_target.inverse_transform(pred_.detach().numpy().reshape(1,-1)).reshape(-1)
    fact_=scale_target.inverse_transform(fact_.detach().numpy().reshape(1,-1)).reshape(-1)
    # print(f'pred: {pred_}, pred: {pred_.shape}, fact: {fact_}, fact: {fact_.shape}')
    accuracy=score(torch.tensor(pred_),torch.tensor(fact_))
    print(f'epoch: {epoch}')
    print(f'[train] total loss: {total_loss}, accuracy: {accuracy}')
    model.eval()
    pred_test=torch.Tensor()
    fact_test=torch.Tensor()
    total_loss=0
    for x,y in test_loader:
        with torch.no_grad():
            x,y=x.to(device),y.to(dtype=torch.float32,device=device)
            optimizer.zero_grad()
            output=model(x[:,:195],x[:,195:])
            loss=F.mse_loss(output,y)        
            total_loss+=loss.item()
            pred_test=torch.hstack((pred_test,output.squeeze()))
            fact_test=torch.hstack((fact_test,y.squeeze()))
    print(f'pred: {pred_}, pred: {pred_.shape}, fact: {fact_}, fact: {fact_.shape}')
    pred_test=scale_target.inverse_transform(pred_test.detach().numpy().reshape(1,-1)).reshape(-1)
    fact_test=scale_target.inverse_transform(fact_test.detach().numpy().reshape(1,-1)).reshape(-1)
    accuracy_test=score(torch.tensor(pred_test),torch.tensor(fact_test))
    Lr.step(total_loss)
    print(f'[test] total loss: {total_loss}, accuracy: {accuracy_test}')
    print(f'*'*40)
        
            
    
        
        