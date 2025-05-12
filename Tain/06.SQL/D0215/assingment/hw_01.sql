# 1번 테이블 생성
set foreign_key_checks=false;
use sqlclass_db;
drop table if exists authors;
create table authors
(author_id int not null,
firstname varchar(20) not null,
lastname varchar(30) not null,
primary key (author_id));
desc authors;

insert into authors(author_id,firstname,lastname)
values
(1,'Paul','Deitel'),
(2,'Harvey','Deitel'),
(3,'Abbey','Deitel'),
(4,'Dan','Quirk'),
(5,'Michael','Morgano');
select * from authors;

# 2번 테이블 생성
drop table if exists titles;
create table titles
(isbn varchar(20) not null,
title varchar(100) not null,
edition_number int not null,
copyright varchar(4) not null,
primary key(isbn));
select * from titles;

insert into titles(isbn,title,edition_number,copyright)
values
('0132151006','Internet & World Wide Web How to Program',5,'2012'),
('0133807800','Java How to Program',10,'2015'),
('0132575655','Java How to Program, Late Objects Version',10,'2015'),
('013299044X','C How to Program',7,'2013'),
('0132990601','Simply Visual Basic 2010',4,'2013'),
('0133406954','Visual Basic 2012 How to Program',6,'2014'),
('0133379337','Visual C# 2012 How to Program',5,'2014'),
('0136151574','Visual C++ How to Program',2,'2008'),
('0133378713','C++ How to Program',9,'2014'),
('0133764036','Android How to Program',2,'2015'),
('0133570924','Android for Programmers: An App-Driven Approach, Volume 1',2,'2014'),
('0132121360','Android for Programmers: An App-Driven Approach',1,'2012');

# 3번 테이블 생성
drop table if exists author_isbn;
create table author_isbn
(author_id int not null,
isbn varchar(20) not null,
foreign key(author_id) references authors(author_id),
foreign key(isbn) references titles(isbn));
desc author_isbn;

insert into author_isbn(author_id,isbn)
values
(1,'0132151006'),
(2,'0132151006'),
(3,'0132151006'),
(1,'0133807800'),
(2,'0133807800'),
(1,'0132575655'),
(2,'0132575655'),
(1,'013299044X'),
(2,'013299044X'),
(1,'0132990601'),
(2,'0132990601'),
(3,'0132990601'),
(1,'0133406954'),
(2,'0133406954'),
(3,'0133406954'),
(1,'0133379337'),
(2,'0133379337'),
(1,'0136151574'),
(2,'0136151574'),
(4,'0136151574'),
(1,'0133378713'),
(2,'0133378713'),
(1,'0133764036'),
(2,'0133764036'),
(3,'0133764036'),
(1,'0133570924'),
(2,'0133570924'),
(3,'0133570924'),
(1,'0132121360'),
(2,'0132121360'),
(3,'0132121360'),
(5,'0132121360');

set foreign_key_checks=True;

# 1
# titles copyrignt >2013
select * from titles;
select title,edition_number,copyright
from titles
where cast(copyright as unsigned integer)>=2013;
-- order by cast(copyright as int) desc;

select cast('2013' as  integer);

# 2
## authors/lastname like 'D%'
select author_id, firstname,lastname
from authors
where lastname like 'D%';

#3
# authors/lastname like '_o%'
select author_id, firstname,lastname
from authors
where lastname like '_o%';

#4
# authors/lastname-firstname
select *
from authors
order by lastname,firstname;

#5
# titles/title fd like '%how to program'/order by title
select *
from titles
where title like '%how to program%'
order by title;

#6
# authors, author_isbn/inner join/ on author_id/출력: firstname,lastname,isbn/정렬:last,first, asc
select firstname,lastname,isbn
from authors a join author_isbn ai on a.author_id=ai.author_id
order by lastname, firstname;

#7
# author_isbn, titles/inner join/on isbn/출력:author_id,	isbn,	title,	edition_number,	copyright/order by isbn desc
select author_id,t.isbn,title,edition_number,copyright
from author_isbn ai join titles t on ai.isbn=t.isbn
order by 2 desc;

#8
# authors(lastname) -> author_isbn -> titles
select firstname,lastname,title,ai.isbn,copyright
from authors a join author_isbn ai on a.author_id=ai.author_id
			   join titles t on ai.isbn=t.isbn
where lastname='quirk';

# 9
select firstname,lastname,title,ai.isbn,copyright
from authors a join author_isbn ai on a.author_id=ai.author_id
			   join titles t on ai.isbn=t.isbn
where lastname='Deitel'and firstname in ('paul','harvey');

# 10
## 'Abbey Deitel', 'Harvey Deitel'
# ---------------------------------------------------
# 따로 출력결과
# [1]
select firstname,lastname,title,ai.isbn,copyright
from authors a join author_isbn ai on a.author_id=ai.author_id
			   join titles t on ai.isbn=t.isbn
where lastname='Deitel'and firstname='abbey';
# [2]
select firstname,lastname,title,ai.isbn,copyright
from authors a join author_isbn ai on a.author_id=ai.author_id
			   join titles t on ai.isbn=t.isbn
where lastname='Deitel'and firstname='harvey';
# -------------------------------------------------
# 공동저자 책 정보 출력
select abbey.title,abbey.isbn,abbey.copyright
from
(select firstname,lastname,title,ai.isbn,copyright
from authors a join author_isbn ai on a.author_id=ai.author_id
			   join titles t on ai.isbn=t.isbn
where lastname='Deitel'and firstname='abbey') abbey 
join
(select firstname,lastname,title,ai.isbn,copyright
from authors a join author_isbn ai on a.author_id=ai.author_id
			   join titles t on ai.isbn=t.isbn
where lastname='Deitel'and firstname='harvey') harvey 
on abbey.title= harvey.title 
order by abbey.title;

