# dict 자료형 전용 함수 즉, method
# [데이터 생성] 아이디와 이름을 입력받아서 저장하기
#  - 3명 저장하기(list, dict)
# [1] list로 담기
personlist=[]
data=input('예) 영어&숫자,홍길동\n 아이디와 이름을 입력해주세요:')
# 아이디와 이름을 분리 후 하나로 묶음
personlist.append(data.split(','))
data1=input('예) 영어&숫자,홍길동\n 아이디와 이름을 입력해주세요:')
# 아이디와 이름을 분리 후 하나로 묶음
personlist.append(data1.split(','))
data2=input('예) 영어&숫자,홍길동\n 아이디와 이름을 입력해주세요:')
# 아이디와 이름을 분리 후 하나로 묶음
personlist.append(data2.split(','))
print(personlist)
