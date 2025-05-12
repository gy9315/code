# 문자열 str type 전용 함수 즉, method
# - n개 문자열 -> 1개 문자열 method: join([str1, str2, str3,...])
# - 1개 문자열로 결과 반환
# -----------------------------------------------------------
# [1] 2개 str data를 1개 str data로 만들기
# - 출력: 'Red-Green'
msg=['Red','Green']
con='-'
con.join(msg)
print(con.join(msg))
# [2] 3개 str data를 1개 str data로 만들기
# - 3개 str data" '2024', '12', '06'
# - 출력: '2024/12/06'
# [2-1] 덧셈 연산으로 만들기
today='2024'+'/'+'12'+'/'+'06'
print(today)
# [2-2] join()method로 만들기
today='/'.join(['2024','12','06'])
# [2] 3개 str data를 1개 str data로 만들기
# - 3개 str data" '2024', '12', '06'
# - 출력: '20241206'
date=''.join(['2024','12','06'])
print(date)