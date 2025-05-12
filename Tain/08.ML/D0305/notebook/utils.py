# 평면/3D에 점을 그려주는 프로그램 설계
'''
    - 사용자가 원하는 위치에 점을 표시하기
    - 점을 표현/저장하는 데이터타입 필요
    - 새로운 데이터 타입 설계
         * 속성/특정/외형: x,y,color,r => 변수: x,y,color,r
         * 행동/기능/역할: 점그리기, 정보출력 => drawing, printinfo()
         * 데이터타입이름: Point

        * 속성/특정/외형: x,y,z,color,r => 변수: x,y,z,color,r
         * 행동/기능/역할: 점그리기, 정보출력 => drawing, printinfo()
         * 데이터타입이름: Point3D'''
# Class 정의
class Point:
    def __init__(self,x,y,color,r):
        self.x=x
        self.y=y
        self.color=color
        self.r=r
        
    def drawing(self):
        # 예) 파란색 점 ●
        print(f'{self.color} ●')
    
    def printinfo(self):
        print(f'{self.x}, {self.y}')
        print(f'{self.r}')
        print(f'{self.color}')
        
class Point3D(Point):
    def __init__(self, x, y, z,color, r):
        super().__init__(x, y, color, r)
        self.z=z
        
    def printinfo(self):
        print(f'{self.x}, {self.y}, {self.z}')
        print(f'{self.r}')
        print(f'{self.color}')
        
if __name__=='__main__':
    black_point=Point(10,10,'black',5)
    red_point=Point3D(5,5,5,'red',5)
    black_point.drawing()
    red_point.drawing()
    black_point.printinfo()
    red_point.printinfo()