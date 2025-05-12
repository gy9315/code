from card import Card
import random
class Gamedealer:
    def __init__(self):
       self.deck=list()
       self.suit_number=13
       
       
    def make_deck(self):
        self.card_suits=['♠','♥','♣','◆']
        self.card_numnber=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        list1=[]
        for x in self.card_suits:
            for y in self.card_numnber:
                list1.append(Card(x,y)) 
        random.shuffle(list1) 
        self.deck=list1        
        
        
    def distribute_card(self,num):
        cardlist_to_player1=[]
        cardlist_to_player2=[]
        for x in range(num):
            cardlist_to_player1.append(self.deck.pop())
        for x in range(num):
            cardlist_to_player2.append(self.deck.pop())
        count=1
        print(f'[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}')
        for x in self.deck:
            if not count%13:
                print(x)
            else: print(f'{x}',end=' ')
            count+=1
        return cardlist_to_player1,cardlist_to_player2
        
if __name__=='__main__':
    dealear=Gamedealer()
    # print(dealear.deck)
    dealear.make_deck()
    # print(dealear.deck)
    dealear.distribute_card(10)
    