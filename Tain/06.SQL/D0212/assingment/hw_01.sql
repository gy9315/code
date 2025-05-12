use sqlclass_db;
show tables;
desc nobel;
select * from nobel;

# 1-1
select year, category, fullname
from nobel
where category='physics' or category='peace'; 
select * from nobel;
# 1-2
select year,category,prize_amount amount,birth_continent,birth_country
from nobel
where fullname='Albert Einstein';
select * from nobel;
# 1-3
select year, fullname,birth_country
from nobel
where year between 1910 and 2010
order by year;
select * from nobel;
# 1-4
select category,fullname
from nobel
where fullname like 'John%';
# 1-5
select * from nobel;
## 1964년 and !=노백 화학상과 의학상 제외 / 수상자 이름 asc
select *
from nobel
where year=1964 and not (category='Physiology' or category='Medicine')
order by fullname asc;

# 1-6
select year,fullname,gender,birth_country
from nobel
where year between 2000 and 2019 and category='Literature';
# 1-7
select * from nobel;
select category, count(*) as nobel_count
from nobel
group by category
order by nobel_count desc;
# 1-8
select distinct year,category
from nobel
where category like'%Medicine%';

# 1-9
select count(distinct year) as total_count
from nobel
where not (category='Physiology' or category='Medicine');

# 1-10
select * from nobel;
select fullname,category,birth_country
from nobel
where gender != 'male';

# 1-11
## 수상자들의 출생 국가별 횟수
select birth_country,count(*) as 횟수
from nobel
group by birth_country;

# 1-12
select *
from nobel
where birth_country='Korea';

# 1-13
select *
from nobel
where birth_continent !='' and birth_continent!='Europe' and  birth_continent!='North America' ; 

# 1-14
# 출신 국가 그룹, 수상횟수(count(*)>10), 모든 정보 출력, 수상횟수 역순
select n.birth_country, count(*) as 횟수
from (select * from nobel where birth_country !='') as n
group by n.birth_country
having count(*)>=10
order by count(*) desc;

# 1-15
# 2회 이상 수상, 이름 공백이 아닌경우, 이름 asc
select n.fullname, count(*) as 횟수
from (select * from nobel where fullname != '') as n
group by n.fullname
having count(*) >=2
order by n.fullname asc;