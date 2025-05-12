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