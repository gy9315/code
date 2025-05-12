# 제어문 - 조건문
# - 특정 조건에 맞을 시 실행되는 경우와 실행되지 않는 코드 구분 실행
# [문] 시험 점수가 60점이면 합격, 아니면 불합격
score=59
data='합격' if score>=60 else '불합격'
print(data)

# [문] 숫자가 양수인지 음수인지 구분해서 출력해주세요
num=1234
data='양수' if num>0 else '음수'
print(f'{num}은 {data}입니다.')

# [문] 나이를 계산해주세요
num='091203-9234567'
# 참: 나이
if num.split('-')[1][0] in '1256':
    year=2024-int('19'+num.split('-')[0][:2])
    print(f'당신의 나이는 {year}입니다.')
elif num.split('-')[1][0] in '3478':
    year=2024-int('20'+num.split('-')[0][:2])
    print(f'당신의 나이는 {year}입니다.')
else: print('주민번호를 잘못입력했습니다.')
