from sklearn.preprocessing import OneHotEncoder
encoder=OneHotEncoder()
# sparse_output=False -> 전체를 0과1로 표현해줌
# drop='first'는 첫번째 카테고리를 삭제시킴 -> 다중공산성 방지
# handle_unknown='ignore' 존재하지 않는 카테고리 무시
encoder.fit([['Female',2],['male',1],['male',3]])
a=encoder.transform([['Female',2],['male',1],['male',3]])