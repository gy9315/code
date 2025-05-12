# 특정 기능 수행 코드의 재사용을 위한 방법: function
# - 자주 사용되는 기능의 코드를 묶음
# - 코드를 1번만 작성 후 필요할 때마다 사용함
# ---------------------------------------------------------
# 기능: 문자열의 기계어 변환 후 반환하는 기능
# 함수이름: convert
# 매개변수: 코드 실행에 사용되는 재료(저장 변수): parameter
# 반환값: 변환된 기계어 코드
def convert(data):
    value=''
    for x in data:
        value=value+bin(ord(x))[2:]
    return value
# -------------------------------------------------------
# 함수사용: 함수 호출 -> 함수명 재료
print(convert('happy'))
# --------------------------------------------------------
# 기능: 2개 정수, 덧셈 후 결과 반환
# 함수: add
# 변수: x,y
# 값: 덧셈 결과=value
def add(x,y):
    value=x+y
    return value

# --------------------------------------------------------
# 기능: 2개 정수, 뺄셈 후 결과 반환
# 함수: sub
# 변수: x,y
# 값:  뺄셈 결과=value
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y if y else '0으로 나눌 수 없습니다.'

print(div(3,0))
# --------------------------------------------------------
# 기능: 입력값 체크 기능
# 함수: check
# 변수: data, kind(체크종류: num/alpha/alnum)
# 값: 정상데이터 여부=value
def check(data,kind):
    if kind=='num':
        return True if data.isnumeric() else False
    elif kind=='alpha':
        return True if data.isalpha() else False
    elif kind=='alnum':
        return True if data.isalnum() else False
    else: return '잘못된 입력입니다.'
print(check('abcd','nd'))
# 2개 정수 나눗셈 후 결롸 출력하는 기능
def twodiv(x,y):
    result=x/y if y else '0으로 나눌 수 없습니다.'
    print(result)
twodiv(4,5)