# module: 관련성이 있는 변수, 함수, 클래스를 모아둔 파일(.py)
# - 사용법
#   import module명(확장자 제외)
#   import module명 as 별칭
# - 위치
#   일반적으로 파일에 제일 상단에 import 구문을 기입(이유: 가독성)
import math
# 임의의 수 추출 기능 필요
import random as r # random 대신에 r를 쓴다
# 모듈 내의 변수, 함수, 클래스 사용
# - 문법: 모듈명.변수명
#         모듈명.함수()
#         모듈명.class
# -----------------------------------------------------------
# 모듈 내의 클래스 사용 => 힙메모리에 저장: 객체(object)
rObject=r.Random()
print('임의의 실수',rObject.random()) # 0<=x<1까지 임의의 수 추출