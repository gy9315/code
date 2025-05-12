use sakila;
show tables;
select * from language;

select language_id,name,last_update from language;
select name from language;

select language_id,
'COMMON' language_usage,
language_id*3.14 lang_pi_value,
upper(name) language_name
from language;
# ----------------------------------------------
# 중복제거
select actor_id from film_actor order by actor_id ;
# distinct 키워드 사용
select distinct actor_id from film_actor order by actor_id ;

# 서브쿼리 만들기(파생테이블)
show tables;

select concat(cust.last_name,',',cust.first_name) as full_name
# 하나의 서브쿼리를 만들기
from 
(select first_name, last_name
from customer where first_name='jessie') as cust;

# 임시 테이블 만들기
# - 휘발성 테이블: 데이터베이스 세션이 닫힐 떄 사람짐
drop table if exists actor_j;
create temporary table actor_j
(actor_id smallint(5),
first_name varchar(45),
last_name varchar(45));
# pandas info()
desc actor_j;
# 임시테이블에 한번에 내용을 입력하는 방법
insert into actor_j
select actor_id, first_name,last_name
from actor where last_name like 'J%';
select * from actor_j;

# ------------------------------------------------------
# 가상테이블 만들기
create view cust_vw as 
select customer_id,first_name,last_name,active from customer;
select * from cust_vw;

# 테이블 연결
# join
select customer.first_name,
customer.last_name,
time(rental_date) as rental_time
from customer inner join rental
on customer.customer_id=rental.customer_id
where date(rental.rental_date)='2005-06-14'
and customer.last_name like 'G%';
# join table 확인
-- select *
-- from customer inner join rental
-- on customer.customer_id=rental.customer_id
-- where date(rental.rental_date)='2005-06-14';


# where 조건 여려개 
desc film;
select title from film 
where rating='g' and rental_duration>=7;


# 열의 데이터를 그룹화와 필터링
# 그룹화: group by
# 필터링: having
# - where은 모든 컬럼에 대한 필터링을 수행
select c.first_name,c.last_name,count(*) rental_count
from customer c inner join rental r on c.customer_id=r.customer_id
group by c.first_name,c.last_name
having count(*)>=40
order by count(*) desc;
# 정렬 자세히 살펴보기
select c.first_name,c.last_name,time(r.rental_date) rental_time
from customer c inner join rental r on c.customer_id=r.customer_id
where date(r.rental_date)='2005-06-14'
-- order by 1,2
# 1번 먼저 정렬 그리고 2번 정렬
order by c.last_name, c.first_name asc;

# 컬럼의 인덱스를 사용하여 정렬
select actor_id,first_name,last_name
from actor
order by 3,2;

# 조건 + 컬럼 인덱스 정렬
select actor_id,first_name,last_name
from actor
where last_name='williams' or last_name='davis';

select distinct customer_id
from rental
where date(rental_date)='2005-07-05';


# 조건문 조건연산자 활용
# [부등조건]
select c.email,r.rental_date
from customer c inner join rental r on c.customer_id=r.customer_id
where date(r.rental_date) != '2005-06-14';

# [범위 조건]
select customer_id,rental_date
from rental
# datetime 속성은 시간 정보 포함임
# 밑에 정보는 2005년 6월 16일 00시까지
-- where rental_date <='2005-06-16'
-- 	  and rental_date >= '2005-06-14';
where date(rental_date) <='2005-06-16'
	  and date(rental_date) >= '2005-06-14';

# [범위조건]
# between
select customer_id,rental_date
from rental
where date(rental_date) between'2005-06-14' and '2005-06-16';

# [or 또는 in()연산]
select title, rating
from film
where rating='g' or rating='pg';
# ---------------------------
use sakila;
# -----------------------
select title, rating
from film
where rating in ('g','pg');
# [문자열 부분 가져오기]
# left right mid 기능 사용하기
select left('abcdefg',3);
select mid('abcdefg',2,3);
select right('abcdefg',3);


# [일치조건]
# 와일드카드 사용하기
# '정확히 한문자': '-'
# 개수에 상관없이 모든 문자 포함: '%'


# [정규표현식: regular expression]
# where 컬럼명 regexp '^[숫자 또는 문자 ]'
# ex) regexp '^[QY]' -> Q 또는 Y로 시작하는 값
# ex) regexp '^[A-Z]' -> A부터 Z로 시작하는 값
# ex) regexp '$[QY]' Q또는 Y로 끝나는 값


# null 값 조회하기
select rental_id, customer_id, return_date
from rental
where return_date is not null;

# [null과 조건 조합]
select distinct rental_id,customer_id,return_date
from rental
where date(return_date) is null or date(return_date) not between '2005-05-01' and '2005-09-01'
order by rental_id;