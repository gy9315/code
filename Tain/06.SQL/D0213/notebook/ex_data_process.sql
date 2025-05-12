use sqlclass_db;
drop table if exists string_tbl;
create table string_tbl
(char_fld char(30),
vchar_fld varchar(30),
text_fld text);


INSERT INTO string_tbl (char_fld, vchar_fld, text_fld)
VALUES ('This is char data',
'This is varchar data',  'This is text data');
select * from string_tbl;

-- update string_tbl
-- set vchar_fld='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas';
select @@session.sql_mode;
set sql_mode='ansi';
select @@session.sql_mode;
update string_tbl
set vchar_fld='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas';
select * from string_tbl;

# 작은 따옴표 포함 문자 처리
update string_tbl
set text_fld='This string didnt''t work, but it does now';
select * from string_tbl;

update string_tbl
set text_fld='This string didnt\'t work, but it does now';
select * from string_tbl;

## 
# delete와 drop 차이점
# delete from string_tbl -> value 갑 지우기
# drop table string_tbl -> table 전체 지우기 

# 문자열의 개수 반환 함수: length()
select length(char_fld) as char_len,
		length(vchar_fld) as vchar_len,
		length(text_fld) as text_len
from string_tbl;


# 문자열 조작
# 원하는 문자열 index확인하기
# 함수: position(문자열 in 컬럼명) and locate(문자열,컬럼명,시작위치)

select position('char' in char_fld)
from string_tbl;
select * from string_tbl;

select locate('is',char_fld,3)
from string_tbl;


# 문자열 크기 비교
# strcmp():str compare
# 대소문자 구분 안함
delete from string_tbl;
insert into string_tbl(vchar_fld)
values
('abcd'),
('xyz'),
('QRSTUV'),
('qrstuv'),
('12345');
select vchar_fld from string_tbl order by 1;



 use sakila;
 select name,name regexp 'y$' end_in_y
 from category;
 
 # 문자열 합치는 함수
 # 함수: concat()
 use sqlclass_db;
 delete from string_tbl;
 
 insert into string_tbl(text_fld)
 values
 ('this string was 29 charaters');
 select * from string_tbl;
 
 update string_tbl
 set text_fld=concat(text_fld,', but now it is longer');
 select text_fld from string_tbl;
 
 
 use sakila;
 select concat
 (first_name,' ',last_name,' has been a customer since ',date(create_date)) cust_narrative
 from customer;
 
 # 문자 사이에 문자 삽입
 # 함수: insert(문자열, 시작위치, 변경길이, 새로운 문자열)
 # -------------------------------------------------
 # position에 컬럼명 대신에 문자열을 입력해도 값이 나온다!!
 # -------------------------------------------------
 select position('e' in 'goodbye');
 select insert('goodbye world',9,0,'creul ') as string;
 select insert('goodbye world',1,7,'creul ') as string;
 
 
 # 문자열 교체
 # 함수: replace(문자열, 기존 문자열, 새로운 문자열)
select replace('goodbye world','goodbye','hello');


# 문자열 추출
# 함수: substr(문자열, 시작위치, 개수)
select substr('goodbye cruel world',9,5);


# 문자열(date 타입)
# str_to_date(formating 사용)
-- update person set birth_date=str_to_date('DEC-21-1980','%b-%d-%Y') where person_id =1;

# casting
# 지정한 값을 다른 데이터 타입으로 변경
create view a as select cast('2019-09-17'as date) as date;
desc a;
##### desc 속성을 알기 위해서 table, 또는 view만 가능한건지
-- desc select cast('2019-09-17'as date) date;
select cast('2019/09/17/15/30/00' as datetime);
select cast('20190917153000' as datetime);


# 날짜 생성 함수
select str_to_date('september 17, 2019','%M %d,%Y');

select str_to_date('04/30/2024','%m/%d/%Y');
select str_to_date('01,5,2024','%d,%m,%Y');
select str_to_date('15:35:00','%H:%i:%s');