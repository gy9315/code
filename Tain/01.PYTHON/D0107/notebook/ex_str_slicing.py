# str 데이터 타입의 슬라이싱
# - 문법: 변수명[시작인덱스:끝인덱스:증감정도(간격)]
#         변수명[0:5:1]
# - 범위: 시작 인덱스 <= N < 끝 인덱스+1
data='abcdefghijklmn'
# 1번 원소부터 8번 원소까지: data[1,9]
print(f'{data} 1번부터 8번까지: {data[1:8]}')
print(f'{data} 1번부터 8번까지: {data[1:8:1]}')
# 'acegikm'만 출력
print(data[0],data[2],data[4],data[6],data[8],data[10], sep="")
print(f'{data} "acegikm"만 출력: {data[0],data[2],data[4],data[6],data[8],data[10]}')
print(f'{data} "acegikm"만 출력: {data[0]}{data[2]}{data[4]}{data[6]}{data[8]}{data[10]}')
print(f'{data} "acegikm"만 출력: {data[::2]}')
# 'A123B123C123D123D999'알파벳만 출력해주세요
num='A123B123C123D123D999'
print(num[0::4])
