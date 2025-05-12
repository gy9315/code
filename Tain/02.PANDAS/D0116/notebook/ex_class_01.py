# class 설계 및 사용

# 사람 정보를 저장하는 데이터 타입 생성
# - class 이름: Person
# - class 속성
#       - 각 인스턴스 변수: name, gender, age, loc
#       - 공유 class: 변수: loc='대한민국'
# - class 기능: eat(), sleep()
# class 내의 self
# - class def에서만 사용
# - python에서 값을 저장해주는 특수한 변수
class Person:
    # 클래스 속성(변수): 정적변수
    loc='대한민국'
    
# python에서 메모리(heap)에 속성으로 저장해주는 기능 method
    def __init__(self,name,age,gender):
        # 인스턴스 변수/속성들
        print('__init__()')
        self.name=name
        self.age=age
        self.gender=gender
    # person class 전용 함수 즉, 메서드
    def eat(self,food):
        print(f' {food}를 먹는다')

    def sleep(self):
        print('잔다')
        
# -------------------------------------------------------
# 객체 생성
# - 문법: 변수명=클래스()
# -------------------------------------------------------
p1=Person('홍길동','12','남')
# method 사용하기
print(p1.name)
p1.sleep()
p1.eat('스파게티')
p2=Person('마징가','15','남')
str

# person 인스턴스들의 속성 읽기와 변경
# - 읽기: 객체변수명.속셩명
# - 변경: 객체변수명.속소명=새로운 값
print(f'[현재이름] {p1.name}')
p1.name='마파두부'
print(f'[현재이름] {p1.name}')
p1=Person()
p1.eat('food')