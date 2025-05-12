# 람다 표현식/익명함수/한줄함수
# - 사용목적: 다른 함수의 인수로 전달되는 경우
# - 형식/문법: lamda 매개변수들:실행코드 및 반환값
# - 많이 사용되는 함수: map(), filter()...
# ----------------------------------------------
def plus_ten(x):
    return x+10
# 람다 표현식/람다 함수
lambda x:x+10
print(plus_ten(5))
print((lambda x:x+10)(5))
print((lambda x,y:x+y)(5,10))

# 내장함수 map(함수명, 여려개의 데이터를 가진 타입): 원소를 함수에 적용
datas=['1','2','3']
datas2=list(map(int,datas))
print(datas,datas2)
# [1,2,3] -> [2,5,10]
list1=[1,2,3]
print(list(map(lambda x:x*x+1,list1)))