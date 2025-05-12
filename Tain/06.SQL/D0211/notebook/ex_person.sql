set foreign_key_checks=false;
use sqlclass_db;
drop table if exists person;
create table person
(person_id smallint unsigned,
fname varchar(20),
lname varchar(20),
eye_color enum('BR','BL','GR'),
birth_date date,
street varchar(30),
city varchar(20),
state varchar(20),
country varchar(20),
postal_code varchar(20),
primary key(person_id));
# 참조하고 있는 foreign key가 있을때 
# set foreign_key_checks=0(False)를 해줘야 한다
alter table person modify person_id smallint unsigned auto_increment;
set foreign_key_checks=true;


# 내용 추가하기
insert into person
(person_id,fname,lname,eye_color,birth_date)
values (null,'William','Turner','BR','1972-05-27');


insert into person
(person_id,fname,lname,eye_color,birth_date,street,city,state,country,postal_code)
values(null,'Susan','Smith','BL','1975-11-02','23 Mapp;eSt','Arlington','VA','USA','20220');
select person.person_id,fname,person.lname,person.birth_date from person;


update person 
set street='1225 TremonSt',
	city='Boston',
	state='MA',
	country='USA',
	postal_code='02138'
where person.person_id =1;
# favorite에 행을 더 추가하기 위해 참조하고 있는 가장 높은 위치에 컬럼을 하나 더 추가한다
insert into person (person_id,fname,lname) values(null,'kevin','kern');
select * from person;
# sql 기본 datetime 약식은 YYYY-MM-DD
-- update person set birth_date='DEC-21-1980' where person.person_id =1;

update person set birth_date=str_to_date('DEC-21-1980','%b-%d-%Y') where person_id =1;
-- select * from person;
set foreign_key_checks=1;
