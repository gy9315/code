use sqlclass_db;
# 연속해서 입력되는 것을 방지하기 위한 drop
drop table if exists books;
# 컬럼과 테이블을 생성
create table books(
		book_id int not null auto_increment,
		title varchar(50),
		publisher varchar(30),
		year varchar(10),
		price int,
		primary key(book_id));

# value값 입력
insert into books(title,publisher,year,price)
values('Operating System Concepts','Whiley','2003',30700);
insert into books(title,publisher,year,price)
values('Head First PHP and MySQL','OReilly','2009',58000),
	  ('C Programming Language','Prentice-Hall','1989',35000);

# 검색 조건: where 사용
select * from books;
select publisher from books;
select * from books where publisher='oreilly';
select * from books where price>=40000 and price <=58000;

# update tabel set 컬럼=변경내용 where 조건
update books set price=30000 where book_id=1;
# 여러줄 update
update books set title='Head First SQL 3rd Edition',price=45000 where book_id=2;

# 행 단위 삭제 delete from table where 조건
-- delete from books where book_id=1;
# 컬럼 추가 alter table 이름 add 컬럼명 dtype
alter table books add author varchar(50);

# author 값 추가하기
update books set author='Jhone willey' where book_id=1;
update books set author='Beightley' where book_id=2;
update books set author='Brian' where book_id=3;

# 컬럼 삭제하기
# alter table 테이블명 drop column 컬럼명
alter table books drop column author;
select * from books;
select user();