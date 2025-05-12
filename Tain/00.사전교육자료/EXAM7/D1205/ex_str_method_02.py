# 문자열 str type 전용 함수 즉, method
# ---------------------------------------------
# [5] 문자/문자 여러개를 변경해주는 method
# - 변수명.replace(old str, new str, count=-1): 변경된 새로운 문자열을 돌려줌
lang='pitihioini'
lang=lang.replace('i','y')
print(lang)
print(lang.replace('i','y'))
# 모든 i를 y로 변경
lang1=lang.replace('i','y', 1)
print(f'모두변경:{lang1}')
# 1개만 i를 y로 변경
lang2=lang.replace('i','y',2)
print(f'모두변경:{lang2}')

# ------------------------------------------- 오류 확인(lang 저장으로 전부 똑같이 나오는)
# lang=lang.replace('i','y')이 이미 바뀐 lang으로 변경되었기에 바꿀문자가 없음
msg='Happy Year! Happy Christmas! Happy Monday'
msg2=msg.replace('pp','PP')
print(msg2)
msg2=msg.replace('Happy', 'Good',2)
print(msg2)
# -------------------------------------------------각각 변경해보기 
