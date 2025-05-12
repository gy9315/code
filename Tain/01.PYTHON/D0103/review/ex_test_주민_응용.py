# [문1] 주민번호를 입력받아서 성별이 남자인지 여부를 출력하세요
# - 주민번호: 000000-0000000
#   * 남자: 1, 3, 5, 7
#   * 여자: 2, 4, 6, 8
for data in range(3):
    num=input('주민번호 14자리를 입력해주세요!!(\'-\'포함하여 입력해주세요):')
    num=num.strip()
    if len(num)==14 and num[6]=='-' and num.split('-')[0].isdigit() and num.split('-')[1].isdigit() and ((num[7] in ('3478') and int(num[:1])<=25) or (num[7] in ('1256') and int(num[:1])<=99)) :
        age=(num[:2])
        if num[7] in ("1357"):
            print('당신의 성별은 남자이며,',end=' ')
            if num[7] in ('15'):
                age='19'+age
                print(f'나이는 {2026-int(age)}세 입니다.')
            else: print(f'나이는 {26-int(age)}세 입니다.')
        else:
            print('당신의 성별은 여자이며,',end=' ')
            if num[7] in ('26'):
                age='19'+age
                print(f'나이는 {2026-int(age)}세 입니다.')
            else: print(f'나이는 {26-int(age)}세 입니다.')
        break
    else: print('주민번호를 양식에 맞게 14자리를 입력 다시 해주세요!!!!!')
