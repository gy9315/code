# 문자열 str type 전용 함수 즉, method
# - 1개 문자열 -> n개 문자열 method: split('공백')
# - n개 문자열 리스트에 담아서 결과 반환
# ------------------------------------------------
msg='Happy New Year 2025'
print(f'msg 타입: {type(msg)}, 원소개수: {len(msg)}개')
# 1개의 문자열을 '공백'을 기준으로 n개 str 데이터로 분리
msgs=msg.split(' ')
print(f'msgs 타입: {type(msgs)}, 원소개수: {len(msgs)}개')
print(msgs)
# 전화번호 분리하기
phone='010-1230-1231'
nums=phone.split('-')
print(f'nums 타입: {type(nums)}, 원소개수: {len(nums)}개')
print(nums)
print(nums[-1:])
# 성과 이름 분리하기
name='홍길동'
last=input('성을 입력하세요:')
last=last.strip()
first=input('이름을 입력하세요:')
first=first.strip()
name=last+first
print(name)
# 특정 문자/문자열 기준으로 분리하기
msg='okGoodokHappyok2025'
msgs=msg.split('ok')
print(msgs)