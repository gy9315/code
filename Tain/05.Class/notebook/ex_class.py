class Counter:
    def __init__(self,name,value):
        self.count=value
        # private변수: 클라스 내부에서만 사용가능
        # - 밖에서 접근 불가, method를 통해서만 값을 접근할 수 있음
        # self.__count=value
        self.count_name=name
        
    def increment(self):
        global total_sum
        total_sum=0
        self.count+=1
        total_sum+=self.count
        
    def reset(self):
        self.count=0
        print(total_sum)
        
    def get(self):
        return self.count

  
a=Counter(name='kdt-7',value=100)
a.increment()
a.increment()
a.reset()
print(f'카운트 값은: {a.count},{a.count_name}')
print(f'카운트 값은: {a.get()}')

class Car:
    def __init__(self,speed,color,model):
        self.speed=speed
        self.color=color
        self.model=model
        
    def drive(self):
        self.speed=60
        

mycar=Car(0,'Blue','E-class')
print('자동차 객체를 생성하였습니다.')
mycar.drive()
print(f'자동차의 속도는: {mycar.speed}')
print(f'자동차의 색상은: {mycar.color}')
print(f'자동차의 모델은: {mycar.model}')



class Bankaccount:
    def __init__(self,bank='Kdt7은행'):
        self.__balance=0
        self.bank=bank
        
    def withdraw(self,amount):
        if self.__balance>=amount:
            if not amount%10000:
                self.__balance-=amount
                global a
                return 1
            else: 
                print('10000원 단위로 다시 입력하세요.')
                return 0
        else: 
            print('통장 잔액이 부족합니다.')
            return 1


          
    def deposit(self,amount):
        if amount%10000==0:
            self.__balance+=amount
            global a
            return 1
        else: 
            print('10000원 단위로 다시 입력하세요.')
            return 0

    def print_balance(self):
        print(f'은행이름: {self.bank}, 통장잔액: {self.__balance}')
        
def main():
    account=Bankaccount()
    while True:
        a=0
        print('-'*10)
        print('1. 입금')
        print('2. 출금')
        print('3. 조회')
        print('4. 종료')
        print('-'*10)
        num=input('메뉴선택:').strip()
        if num=='1':
            while a==0:
                amount=input('입금할 금액을 10000원 단위로 입력하세요:').strip()
                if amount.isnumeric():
                    a=account.deposit(int(amount))   
                else: 
                    print('숫자를 입력해주세요.')
        elif num=='2':
            while a==0:
                if amount.isnumeric():
                    amount=input('출금할 금액을 10000원 단위로 입력하세요:')
                    a=account.withdraw(int(amount))
                else: 
                    print('숫자를 입력해주세요.')
        elif num=='3':
            account.print_balance()
        elif num=='4':
            print('프로그램을 종료합니다.')
            break
        else:
            print('올바른 메뉴선택을 해주세요!')
main()