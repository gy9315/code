# List 자료형
# - 다양한 종류의 여러 개의 데이터를 저장하는 타입
# - 형식: [data1,data2,...]
# - 원소/요소 식별을 위해서 index와 slicing을 사용함
# ------------------------------------------------
# 리스트 indexing
fruits=['사과','딸기','바나나','키위','수박']
f1='사과'
f2='딸기'
f3='바나나'
f4='키위'
f5='수박'
# 원소/요소 읽어오기 => 변수명[인덱스번호]
# - 사과
print(fruits[0],fruits[-5])
# 키위
print(fruits[3],fruits[-2])
# 사과, 수박
print(fruits[0],fruits[-1])
# 사과, 딸기, 바나나 가져오기
print(fruits[:3])
# 기말고사 3과목 정수를 저장
score=[98,100,77,60,40,20]
print(score[0],score[1],score[2])
print(score[:])
# 짝수번째 요소(점수)만 출력
print(score[1::2])