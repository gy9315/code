select 1 num ,'abc' str
union
select 9 num,'xyz' str

# -------------------------
use sakila;
select 'cust' type1, c.first_name,c.last_name
from customer c
union all
select 'actr' type1, a.first_name, a.last_name
from actor a;

# -------------------------
# actor table union all(합집합 + a)
select 'actr1' as type, a.first_name, a.last_name
from actor a
union all
select 'actr2' as type, a.first_name,a.last_name
from actor a;

select 'cust' type1, c.first_name,c.last_name
from customer c
where c.first_name regexp 'a$' and c.last_name like 'D%'
union all
select 'actr' type1, a.first_name, a.last_name
from actor a
where a.first_name regexp 'a$' and a.last_name like 'D%';
# ----------------------------
# union(합집합)
select c.first_name,c.last_name
from customer c
where c.first_name like 'J%' and c.last_name like 'D%'
union
select a.first_name, a.last_name
from actor a
where a.first_name like 'J%' and a.last_name like 'D%';
# ----------------------------
# intersect(교집합)
select c.first_name,c.last_name
from customer c
where c.first_name like 'd%' and c.last_name like 't%'
intersect
select a.first_name, a.last_name
from actor a
where a.first_name like 'd%' and a.last_name like 't%';
# except(차집합)
select a.first_name, a.last_name
from actor a
where a.first_name like 'j%' and a.last_name like 'd%'
except
select c.first_name,c.last_name
from customer c
where c.first_name like 'j%' and c.last_name like 'd%';
# 복합 쿼리의 정렬
select c.first_name f,c.last_name l
from customer c
where c.first_name regexp 'a$' and c.last_name like 'D%'
union all
select a.first_name, a.last_name
from actor a
where a.first_name regexp 'a$' and a.last_name like 'D%'
order by f,l;
### 복합 쿼리 별칭 사용이유
# 집합 만들게 되었을때 기존 테이블을 참조하고 있는 컬럼명은 사용불가
# 새로운 별칭을 만들어서 컬럼명을 새로 만들어서 사용 가능
# c.first_name의 원래 컬럼명인 first_name 사용가능

# -> 컬럼명을 통해 순서를 만들던가 값을 비교 하고 싶을때 별칭 또는 기존 컬럼명을 사용해야한다!!!!!