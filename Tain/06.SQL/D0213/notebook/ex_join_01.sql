show databases;
use sakila;
show tables;
select count(*) as 숫자
from (select c.first_name,c.last_name,a.address
from customer c join address a) as n;


# inner join
select *
from customer c join address a 
on c.address_id= a.address_id;

# 3개 이상 테이블(inner join)
select *
from customer c join address a on c.address_id=a.address_id
				join city ct on a.city_id=ct.city_id;

# 3개 이상 테이블(서브쿼리 사용)
select *
from address a join city ct on a.city_id=ct.city_id
where a.district='california';

select c.first_name,c.last_name,addr.address,addr.city,addr.district
from customer c join 
(select a.address_id,a.address,ct.city,a.district
from address a join city ct on a.city_id=ct.city_id
where a.district='california') as addr
on c.address_id=addr.address_id;

# 테이블 재사용
select f.film_id,f.title,a.first_name,a.last_name
from film f join film_actor as fa on f.film_id=fa.film_id
			join actor a on fa.actor_id=a.actor_id
where (a.first_name='cate' and a.last_name='mcqueen') or (a.first_name='cuba' and a.last_name='birch')
order by film_id;


# 두 배우가 동반 출연한 영화만 검색
select cuba.title
from 
(select f.film_id,f.title from film f join film_actor as fa1 on f.film_id=fa1.film_id
			join actor a on fa1.actor_id=a.actor_id
where a.first_name='cate' and a.last_name='mcqueen') as cate
join
(select f.film_id,f.title
from film f join film_actor as fa2 on f.film_id=fa2.film_id
			join actor a on fa2.actor_id=a.actor_id
where a.first_name='cuba' and a.last_name='birch') as cuba
on cate.film_id=cuba.film_id;
# ----------------------------------------------------------------

