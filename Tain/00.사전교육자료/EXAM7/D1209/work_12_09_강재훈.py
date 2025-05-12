# [1]
jumsu=[98,72,90,82,88]
# [2]
str_='Good Luck Happy New Year'
str_=str_.split(' ')
print(f'{len(str_)}개, {str_}')
# [3]
score=input('중간고사 5과목 점수를 입력해주세요(ex. 10,20,30):')
print(type(score))
score=score.split(',')
print(score)
# [4]
list_=[1,3,5,7,9,11]
list_.append(13)
list_.append(15)
print(list_)
# [5]
list_=[1,3,5,7,9,11]
list_.remove(5)
print(list_)
# [6]
list_=['kiwi','banana','orange','apple']
list_.sort(reverse=1)
print(list_)
# [7]
list_=[10,20,30,15,20,40]
list_.reverse()
print(list_)
# [8]
list_=[]
num=int(input('좋아하는 숫자를 입력해줘:'))
list_.append(num)
num=int(input('좋아하는 숫자를 입력해줘:'))
list_.append(num)
num=int(input('좋아하는 숫자를 입력해줘:'))
list_.append(num)
print(list_)
# [9]
list_=[1,2,3,4,5,6]
list_.remove(list_[0])
list_.remove(list_[0])
list_.remove(list_[0])
list_.remove(list_[0])
list_.remove(list_[0])
list_.remove(list_[0])
# ---------------------------------------
print(list_)
list_=[1,2,3,4,5,6]
list_.clear()
print(list_)
# ---------------------------------------
list_=[1,2,3,4,5,6]
del list_[:]
print(list_)
# [10]
list_=[1,2,3,4,5,6]
list_.insert(1,100)
list_.append(200)
print(list_)
[11]
list_=['Good',32,False,8.91,'A',32]
print(list_.index(8.91))
list_.remove(32)
print(list_)
list_.remove(32)
print(list_)
# [12]
list_=['가나다','한글','가방','국가','쏘핫']
print(f'최대값: {max(list_)}')
print(f'최소값: {min(list_)}')
print(f'개수: {len(list_)}')