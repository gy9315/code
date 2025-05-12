# package
# - 동일 카테고리에 여러 개의 모듈을 묶어 둔것
# - 범위: 패키지명.모듈명
# - 사용: import 패키지명.모듈명
import urllib
import urllib.request as u_request

# 기능 코드
# ----------------------------------------
u_request.urlretrieve('https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                            'logo.png')
def calc(*a,b:str):
    list1=[z for z in a]
    if b=='+':
        x=0
        for y in list1:
            x+=y
        return x
    if b=='*':
        x=1
        for y in list1:
            x*=y
        return x
    if b=='!':
        x=1
        for y in range(1,list1[0]+1):
            x*=y
        return x            
print(calc(5,b='!'))