# 파일입출력 - 일반 파일
# 쓰기 모드
'''
file=open('open.txt',mode='w',encoding='utf-8')
file.writelines(['Good Luck\n2025 행복한오늘'])
file.close()
'''
# =============================================
'''
file=open('open.txt',mode='a',encoding='utf-8')
file.writelines(['Good Luck\n2025 행복한오늘'])
file.close()
'''
# ============================================
# mode=x는 기존 파일 존재 시 오류발생
'''
file=open('open2.txt',mode='x',encoding='utf-8')
file.writelines(['Good Luck\n2025 행복한오늘'])
file.close()
'''
# ===========================================
# [권장사항]
# with ~ as: 파일 close 자동 처리함
'''
with open('open2.txt',mode='w',encoding='utf-8') as file:
    file.write('Good')
    file.write('Bye')
'''
# ============================================
# with open('open2.txt',mode='r',encoding='utf-8') as file:
#     a=file.read()
#     print(a)
# ==========================================
# open.txt.본사본 만들기
'''
with open('./open.txt',mode='r',encoding='utf-8') as file:
    a=file.readlines()
with open('copy.txt',mode='w',encoding='utf-8') as file1:
    file1.writelines(a)
'''
# [bytes 자료형]
# - 바이너리 데이터 관련 자료형
# - 식별자: b'0x\XXX', b'str'
# print(hex(17))
# print(bytes([17]))
# int_num=17
# # ==========================================
# print(f"[1Bytes, Little, unsigned]: {int_num.to_bytes(length=1,byteorder='little')}")
# print(f"[2Bytes, Little, unsigned]: {int_num.to_bytes(length=2,byteorder='little')}")
# print(f"[2Bytes, Little, signed]: {int_num.to_bytes(length=2,byteorder='little',signed=True)}")
# print(f'*'*40)
# print(f"[1Bytes, big, unsigned]: {int_num.to_bytes(length=1,byteorder='big')}")
# print(f"[2Bytes, big, unsigned]: {int_num.to_bytes(length=2,byteorder='big')}")
# print(f"[2Bytes, big, signed]: {int_num.to_bytes(length=2,byteorder='big',signed=True)}")
# # =========================================
# print(b'AB'.decode())
# print(bytes('ab',encoding='utf-8'))
# # ========================================
# a=bin(10000000)
# print(str(a))
file=open('./open.txt',encoding='utf-8')
a=file.readlines(1)
b=file.readlines(1)
c=file.readlines(1)
print(a)
print(b)
print(c)
file.close()