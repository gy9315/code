# 문자열 str type 다루기- 멤버연산자
# - A in B: A문자가 B문자 안에 있는지 확인
# - 결과: T or F
# - A not in B: A문자가 B문자 안에 없는지 확인 
# -------------------------------------------
msg='Good luck 2025'
# [1] 문자 1개 존재 여부
print('G'in msg)
print('g'in msg)
print(f'G 문자 뒤에 공백 넣은 값:{"G " in msg}')
print(f'd 문자 뒤에 공백 넣은 값:{"d " in msg}')
# [2] 여러개 문자 존재 여부
print('Good'in msg)
print('good'in msg)
# [3] 문자 1개 존재 여부
print('g'not in msg)
print('G'not in msg)
# [활용] 주민번호에서 남자인지 출력하기
# -출력형태: 남자 T/F
# - 1 or 3: 남자, 2 or 4: 여자
ad='112231-5234143'
print(f'남자 {ad[7]=="1" or ad[7]=="3"}')
print(f'남자 {ad[7] in "13"}')
# print(f'{1 in 1}') * 숫자 안에 숫자는 오류: 숫자는 원소로 나눌 수 없음
# [활용] 주민번호에서 성별이 잘못된 주민번호 확인
# -출력형태: 올바른 주민번호 T/F
print(f'성별 올바르게 입력여부: {ad[7] in "1234"}')
print(f'잘못된 주민번호 여부: {ad[7] not in "1234"}')
