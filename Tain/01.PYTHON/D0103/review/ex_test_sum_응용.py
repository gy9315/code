num=[]
for b in range(3):
    list=input('숫자 3개를 입력해주세요:')
    if list.count(',')==2 and len(list)>=5:
        if list.split(',')[0].strip().isdecimal() and list.split(',')[1].strip().isdecimal() and list.split(',')[2].strip().isdecimal():
            for data in range(3):
                num.append(int(list.split(',')[data]))
            print(sum(num))
            break            
        else: print('숫자를 정확하게 입력해주세요!!')
    else: print('숫자 3개와 쉼표(,)을 사용하여 구분하여 정확하게 입력해주세요!!')
