# 함수-사용자 정의 함수
# - 자주 사용되는 기능 코드를 재사용하기 위해서
#   코드를 작성하고 사용할 수 있도록 이름을 붙임
# - 사용: 이름(매개변수,...,매개변수n)
# -----------------------------------------------
# 메모리에 데이터 저장하는 문법
# 변수명=데이터
# 문법/형식
# ---------------------------------------------
# def 코드지정이름/라벨(매개변수1,...,매개변수2)
#   들여쓰기-실행코드
#           .
#           .
#           .
#   들여쓰기-실행코드
#   return-결과값
# ----------------------------------------------
# 기능: 2개의 정수를 덧셈 후 덧셈 결과를 반환가능
# 함수이름: plus
# 변수: num1(숫자), num2(숫자)
# 결과: num1+num2(int)

def plus(num1:int=0,num2:int=0):
    result=num1+num2
    return result
print(plus(10))
# 함수사용: 함수 실행 즉, 호출
# - 문법: 함수 이름(매개변수에 전달한 데이터)
# 함수에 전달되는 데이터: argument

# # ----------------------------------------------
# 기능: 0개 ~ n개 정수 덧셈 화면 출력
# 함수이름: plus
# 변수: *num
# 결과: 화면 출력으로 반환값

def plus(*nums):
    print(type(nums))
plus()