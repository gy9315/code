# 제어문-조건문
# [문제] 주민번호를 입력받아서 아래와 같은 결과를 출력하세요
# [출력]
# - 나이: 21세
# - 성별: 여자
# - 생일: 11월 9일
num=input('예시. 000000-0000000\n 주민번호를 입력하세요:').strip()
if '-' in num and len(num)==14:
    if num.split('-')[0].isnumeric and num.split('-')[1].isnumeric:
        num=num.split('-')
        year=num[0][0]+num[0][1]
        year1=2024-(1900+int(year)) if num[1][0] in '1256' else 2024-(2000+int(year))
        print(f'나이: {year1}세')
        gen='남자' if num[1][0] in '1357' else '여자'
        print(f'성별: {gen}')
        mon=num[0][2]+num[0][3]
        day=num[0][4]+num[0][5]
        print(f'생일: {int(mon)}월 {int(day)}일')

    else: 
        print('형식에 맞지 않는 주민번호입니다.')

else:
    print('형실에 맞지 않는 주민번호입니다.')
    num=input('예시. 000000-0000000\n 주민번호를 입력하세요:').strip()
    if '-' in num and len(num)==14:
        if num.split('-')[0].isnumeric and num.split('-')[1].isnumeric:
            num=num.split('-')
            year=num[0][0]+num[0][1]
            year1=2024-(1900+int(year)) if int(year)>=50 else 2024-(2000+int(year))
            print(f'나이: {year1}세')
            gen='남자' if num[1][0] in '13' else '여자'
            print(f'성별: {gen}')
            mon=num[0][2]+num[0][3]
            day=num[0][4]+num[0][5]
            print(f'생일: {int(mon)}월 {int(day)}일')

    else: 
        print('형식에 맞지 않는 주민번호입니다.')



# year=num[0][0]+num[0][1]
# year1=2024-(1900+int(year)) if int(year)>=50 else 2024-(2000+int(year))
# print(f'나이: {year1}세')
# gen='남자' if num[1][0] in '13' else '여자'
# print(f'성별: {gen}')
# mon=num[0][2]+num[0][3]
# day=num[0][4]+num[0][5]
# print(f'생일: {mon}월 {int(day)}일')
