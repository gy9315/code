'''
FILENAME: utils.py
DESCRIPTION: 데이터 분석에 자주 사용되는 기능의 함수들 관련 모듈
DATE: 2025.01.15.
HISTORY:    WRITER      DATE            DESC
            KANG        20205.01.03     print_info() 추가
'''
# 기능: 개발 정보 출력
# 이름: print_info()
# 변수: -
# 결과: -
def print_info():
    print('--------------------')
    print('회사명: KNU')
    print('연락처: 010-1111-2222')
    print('version: v1.0')
    print('--------------------')
    
# 함수호출/사용
if __name__=='__main__':
    print_info()
    print('utils.py',__name__)