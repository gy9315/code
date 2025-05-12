# [1]
def club(a,b,c,d,e):
    print(f'이름: {a}, 소속: {b}, 포지션: {c},{d},{e}')
    
club("손홍민", "EPL토트넘", "CF", "LW", "RW")
# [2]
def search_month(*a):
    data2=[1,2,3,4,5,6,7,8,9,10,11,12]
    data1=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    data=dict(zip(data1,data2)) 
    for x in a:
        print(f'{data[x.capitalize()]}월',end=' ')    
search_month('May','Jun')
# [3]
def info_user(**a):
    data1=['이름','휴대전화','전화','팩스','이메일','회사주소','집주소','생일']
    data2=['','','','','','','','']
    data=dict(zip(data1,data2))
    for x in a:
        data.update(a)
info_user(휴대전화='010-1111-2222')
