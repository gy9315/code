import random
from card import Card
class Player:
    def __init__(self,name):
        self.name=name
        self.holding_card_list=list()
        self.open_card_list=list()
        
    # def __repr__(self):
    #     return f'Open card list: {len(self.open_card_list)}\n{self.open_card_list}\n\nHolding card list: {len(self.holding_card_list)}'
        
    def add_card_list(self,card_list):		
        self.holding_card_list.extend(card_list)
								
    def	check_one_pair_card(self):
        self.holding_card_list
        check_number=[]
        for x in self.holding_card_list:
            check_number.append(x.number)
        check=[]
        for x in check_number:
            if check_number.count(x)>=2:
                check.append(x)
        check=set(check)
        self.check_number_rept={}
        for y in check:
            idx=[]
            for x in range(len(check_number)):
                if check_number[x]==y:
                    idx.append(x)
            self.check_number_rept[y]=idx
        
                 
    def display_two_card_lists(self):
        # 트리플 또는 나머지 나누기
        
        for x in self.check_number_rept.values():
            if len(x)==3:
                random.shuffle(x)
                for y in x[:2]:
                    display_card=self.holding_card_list.pop(y)
                    self.holding_card_list.insert(y,0)
                    self.open_card_list.append(display_card)
            else:
                for y in x:
                    display_card=self.holding_card_list.pop(y)
                    self.holding_card_list.insert(y,0)
                    self.open_card_list.append(display_card)
        for x in range(self.holding_card_list.count(0)):
            self.holding_card_list.remove(0)
            
    def print_status_card(self):
        print(f'[{self.name}] Open card list: {len(self.open_card_list)}')
        count=1
        for x in self.open_card_list:
            if not count%13:
                print(x)
            else: print(f'{x}',end=' ')
            count+=1
        print('\n')
        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')
        count=1
        for x in self.holding_card_list:
            if not count%13:
                print(x)
            else: print(f'{x}',end=' ')
            count+=1
        print('\n')
        

    
    

        