# # 반려동물 관리 프로그램 개발
# - 반려동물: 강아지,고양이,토끼,물고기,...
# - 반려동물 데이터를 표현/저장하는 타입 필요
#     (1) 강아지
#         * 특정/속성/성질/외형: 품종, 털색상, 무게, 나이,성별,이름
#         * 행동/기능/동작: 짖는다, 문다, 꼬치친다, 죽는척하기

# - 추상화를 기반으로 코드작성 즉, 클래스 정의 
#     * 특정/속성/성질/외형: 변수 -> field, attribute 
#     * 행동/기능/동작: 함수 -> method
class Dog:
    def __init__(self,kind,coat_color,eye_color,weight, age,gender,name):
        print('dog__init__()')
        self.kind=kind
        self.coat_color=coat_color
        self.eye_color=eye_color
        self.weight=weight
        self.age=age
        self.gender=gender
        self.name=name
        
    def bark(self):
        print(f'{self.name}가 멍멍 짖는다.' )   
        
if __name__=='__main__':
    myDog=Dog('차우차우','검은색','갈색',10,5,'male','몽이')
    myDog.bark()

#     (1) 강아지
#         * 특정/속성/성질/외형: 품종, 털색상, 무게, 나이,성별,이름
#         * 행동/기능/동작: 밥먹기, 잠자기, 꾹꾹이
class Cat:
    def __init__(self,kind,coat_color,eye_color,weight, age,gender,name):
        print('dog__init__()')
        self.kind=kind
        self.coat_color=coat_color
        self.eye_color=eye_color
        self.weight=weight
        self.age=age
        self.gender=gender
        self.name=name
        
    def eat(self,food):
        print(f'{self.name}가 {food}을 먹는다.' )   
        
    def sleep(self):
        print(f'{self.name}가 잠을 잔다.' )  
if __name__=='__main__':
    myDog=Dog('차우차우','검은색','갈색',10,5,'male','몽이')
    myDog.bark()
    cat=Cat('길고양이','검은색','파란색',5,4,'female','귀염둥이')
    cat.sleep()
    cat.eat('밥')