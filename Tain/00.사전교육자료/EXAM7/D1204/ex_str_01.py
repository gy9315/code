# 문자열 str type 데이터 다루기
# ------------------------------------
# 문자열 표현방버
# ------------------------------------
# [1]''사이에 데이터는 str type
name='hong'
print(name)
# [2]""사이에 데이터는 str type
name1="hong"
print(name1)
# [3]' 또는 " 3개로 여러 줄 문자열 저장
message='''오늘은 좋은날        
내일도 좋은날'''
message1=''' 오늘은 좋은날
             내일도 좋은날
             2025년도 좋은날'''
message2='''
            서시
                윤동주
         하늘 우러러
         한점 부끄럼이
         업기를'''
print(message)
# 공백문자(whitespace)도 문자 ★
print(message1)
print(message2)