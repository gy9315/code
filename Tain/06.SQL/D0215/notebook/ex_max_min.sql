use sakila;
select customer_id, count(*)
from rental
group by customer_id
order by 2 desc;


# 고유한 값 계산
select count(customer_id),count(distinct customer_id)
from payment;

# 집계함수 사용
select customer_id, max(datediff(return_date,rental_date))
from rental
group by customer_id;
select * from rental;
# null 처리방법
# 사칙연산에서 null값은 계산안함
drop table if exists number_tbl;
create table number_tbl
(val int);

insert into number_tbl
values
(1),
(2),
(4),
(null);
select * from number_tbl;

select count(*),count(val),sum(val),max(val),min(val),avg(val)
from number_tbl;

# 다중 열 그룹화
select fa.actor_id, f.rating, count(*)
from film_actor fa join film f on fa.film_id=f.film_id
group by fa.actor_id, f.rating
order by 1,2;

select actor_id from film_actor;

# 그룹화 표현식
select extract(year from rental_date) year, count(*) how_many
from rental
group by extract(year from rental_date);

select month(rental_date) year, count(*) how_many
from rental
group by month(rental_date);

# 총합결과 나타내는 방법
# with rollup
select fa.actor_id, f.rating, count(*)
from film_actor fa join film f on fa.film_id=f.film_id
group by fa.actor_id, f.rating with rollup
order by 1,2;


# 두가지 필터 사용
select fa.actor_id, f.rating, count(*)
from film_actor fa join film f on fa.film_id=f.film_id
where f.rating in ('g','pg')
group by fa.actor_id, f.rating with rollup
having count(*) >9;

# 지불 횟수 확인, 총 금액 계산
select * from payment;

select customer_id, count(*), sum(amount)
from payment
group by customer_id;

use sakila;
desc language;