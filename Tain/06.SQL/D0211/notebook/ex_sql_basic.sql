-- salkila 데이터베이스 선택
use sakila; # ctrl + enter 한 라인 실행
show tables;

use sqlclass_db;
create table books(
	book_id int not null auto_increment,
	title varchar(50),
	publisher varchar(30),
	year varchar(10),
	price int,
	primary key(book_id));