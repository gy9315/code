# # 사람:
#     * 변수: 성별,이름,나이,키,주소
#     * method: 기본정보
# # 학생:
#     * 변수: 학업성적, 학교  
#     * method: 학업성적, 학교
# # 의사:
#     * 변수: 결혼유무,병원과,직장위치,부동산  
#     * method: 직장정보, 재산

class Human:
    def __init__(self,gender,name,age,tall,address):
        self.gender=gender
        self.name=name
        self.age=age
        self.tall=tall
        self.address=address
    
    def __repr__(self):
        return f'성별: {self.gender}\n이름: {self.name}\n나이: {self.age}\n  키: {self.tall}\n주소: {self.address}'

    def eating(self,food):
        print(f'{self.name}이 {food}을 먹는다')
        
class Student(Human):
    def __init__(self, gender, name, age, tall, address,score,school_name):
        super().__init__(gender, name, age, tall, address)
        self.score=score
        self.school_name=school_name
    
    def study(self,subject,time,where):
        print(f'{self.name}이 {where}에서 {time}시간 동안 {subject}과목을 공부할 예정이다.')        
        
    def school_info(self):
        if self.age>=14 and self.age<=16:
            grade='중학교'
            grade_info=self.age-13
        elif self.age>=17 and self.age<=19:
            grade='고등학교'
            grade_info=self.age-16
        else: 
            grade='초등학교'
            grade_info=self.age-7
        print(f'이름: {self.name}\n학교: {self.school_name+grade}\n학년: {grade_info}')

class Doctor(Human):
    def __init__(self, gender, name, age, tall, address,department,hospital_address,real_estate,marry:bool=False):
        super().__init__(gender, name, age, tall, address)
        self.department=department
        self.hospital_address=hospital_address
        self.real_estate=real_estate
        self.marry=marry
        
    def __repr__(self):
        return f'성별: {self.gender}\n이름: {self.name}\n나이: {self.age}\n결혼유무: {self.marry}\n  키: {self.tall}\n주소: {self.address}'

    def hospital_info(self):
        return f'주소: {self.hospital_address}\n 진료과목: {self.department}'
    
    def real_estimate_info(self):
        return f'재산: {self.real_estate}'
        
        
if __name__=='__main__':
    s1=Student('male','강재훈',18,182,'대구',100,'남주')
    print(s1)
    s1.school_info()
    