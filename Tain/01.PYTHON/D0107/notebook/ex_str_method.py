# str 데이터 타입 전용 method: format()
# - 기능: 원하는 형식/양식/형태의 문자열 생성
# - 문법: ' {}{}'.format(data1,data2)
job='학생'
work_year=4
# 출력순서가 동일한 경우 인덱스 생략 가능
msg='나는 {}년차 {}입니다'.format(work_year,job)
# 출력순서가 다른 경우 인덱스 기입 필수수
msg2='나의 직업은 {1}이고, {0}년째 일하고 있다.'.format(work_year,job)
print(msg,msg2,sep='\n')
# format(name=data1, name2=data2): 문자열 {}사이에 데이터의 name 기입
msg3='나는 {y}년차 {j}이다.'.format(j=job,y=work_year)
print(msg3)
print(f'나는 {job:>10}이고 {work_year:10}입니다.')
# 정렬: 왼쪽, 오른쪽, 가운데 정렬
# - 사용법: {(데이터):(정렬기호) (칸수)}
#           {:<10} {:>10} {:^10}
month='12'
day='20'
data='나의 생일은 {}월 {}일입니다.'.format(month,day)
data1='나의 생일은 {:<6}월 {:<6}일입니다.'.format(month,day)
data2='나의 생일은 {:>6}월 {:>6}일입니다.'.format(month,day)
data3='나의 생일은 {:^6}월 {:^6}일입니다.'.format(month,day)
data4='나의 생일은 {:3}월 {:3}일입니다.'.format(month,day)
data5='나의 생일은 {:6}월 {:6}일입니다.'.format(month,day)
print(data,data1,data2,data3,data4,data5,sep='\n')
# 정렬: 왼쪽, 오른쪽, 가운데 정렬
# 공백문자: 칸수보다 데이터가 작은 경우 생기는 공백에 들어갈 문자
# - 사용법: {(데이터):(공백문자) (정렬기호) (칸수)}
#           {:_<10} {:>_10} {:^a10}
data='나의 생일은 {}월 {}일입니다.'.format(month,day)
data1='나의 생일은 {:1<6}월 {:1<6}일입니다.'.format(month,day)
data2='나의 생일은 {:1>6}월 {:1>6}일입니다.'.format(month,day)
data3='나의 생일은 {:1^6}월 {:1^6}일입니다.'.format(month,day)
print(data,data1,data2,data3,sep='\n')
# 정렬: 왼쪽, 오른쪽, 가운데 정렬
# 공백문자: 칸수보다 데이터가 작은 경우 생기는 공백에 들어갈 문자
# - 사용법: {(데이터):(공백문자) (정렬기호) (칸수)}
#           {:_<10} {:>_10} {:^a10}
avg=89.12345
data1='나의 평균은 {:0<f}입니다.'.format(avg)
data2='나의 평균은 {:0<f}입니다.'.format(avg)
print(data1,data2,sep='\n')