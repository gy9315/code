# 제어문-조건문
# - 목적: 조건에 따라 실행되는 코드가 다름
# - 종류: (단일)조건문, 다중조건문, 중첩조건문
# [1] 자격증 시험에서 60점 이상이면 합격 그렇지 않으면 불합격
# - 임의로 점수를 정해서 합격/불합격 코드를 작성하세요.
# score=90
# if score>=60:
#     print(f'{score}점은 합격입니다.')
# else:
#     print(f'{score}점은 불합격입니다.')
# # [2] 성적을 입력받아서 학점을 출력해주세요
# #  - 학점: A,B,C,D,F
# score=int(input('성적을 입력해주세요:'))
# if score>=90:
#     print(f'학점은 A입니다.')
# elif score>=80:
#     print(f'학점은 B입니다.')
# elif score>=70:
#     print(f'학점은 C입니다.')
# elif score>=60:
#     print(f'학점은 D입니다.')
# else:
#     print(f'학점은 F입니다.')
str='3'
print(str.isdigit())
