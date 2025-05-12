use economic_condition;
select count(번호) from utf;
select * from utf;
# 생겨난 음식점 수
# 속성변경(date타입)
update utf set 인허가일자=concat(인허가일자,'-01');
update utf set 폐업일자=concat(폐업일자,'-01');
update utf set 인허가일자=replace(인허가일자,'-01','1995-01-01') where 인허가일자='-01';
update utf set 인허가일자=cast(인허가일자 as date);
update utf set 폐업일자=replace(폐업일자,'-01','') where 폐업일자='-01';
update utf set 폐업일자=cast(폐업일자 as date) where 폐업일자!='';
select count(*) from utf;
# 주소지 통일시키기
# [1] 최빈값 찾기
CREATE VIEW most_common_address AS
SELECT 개방자치단체코드, 소재지전체주소,
       COUNT(*) AS cnt,
       ROW_NUMBER() OVER (PARTITION BY 개방자치단체코드 ORDER BY COUNT(*) DESC) AS rn
FROM utf
GROUP BY 개방자치단체코드, 소재지전체주소;
# [2] 최빈값 선택
CREATE VIEW most_common_address_filtered AS
SELECT 개방자치단체코드, 소재지전체주소
FROM most_common_address
WHERE rn = 1;
# [3] update
UPDATE utf a
JOIN most_common_address_filtered b
ON a.개방자치단체코드 = b.개방자치단체코드
SET a.소재지전체주소 = b.소재지전체주소
where a.소재지전체주소='';

# -------------------------------------------------------------
# 소재지 비워져 있는 주소칸 채우기
# 1번 innerjoin으로 테이블 만든다
# 2번 null 값에 주소값 집어넣는다
update 
utf a join (select 개방자치단체코드 , max(소재지전체주소) as 소재지전체주소 from utf where 소재지전체주소!='' group by 개방자치단체코드) as b
on a.개방자치단체코드 = b.개방자치단체코드
set a.소재지전체주소=b.소재지전체주소
where a.소재지전체주소='';

select * from utf where 소재지전체주소='';

# 파이썬 작업 ->
# 새로 생긴 음식점 view만들기
drop view if exists open_food;
create view open_food as
select 개방자치단체코드,year(인허가일자) as 연도,count(*) as 개수, SUBSTRING_INDEX(소재지전체주소, ' ', 2) as 주소
from utf
group by 개방자치단체코드, year(인허가일자),소재지전체주소
order by 개방자치단체코드,year(인허가일자);

select * from open_food where 주소 like '%전북%';

# 각 연도에 폐업음식점 view 만들기
drop view if exists close_food;
create view close_food as
select 개방자치단체코드, year(폐업일자) as 연도,count(*) as 개수,SUBSTRING_INDEX(소재지전체주소, ' ', 2) as 주소
from utf 
where 폐업일자!=''
group by 개방자치단체코드,year(폐업일자),소재지전체주소
order by 개방자치단체코드,year(폐업일자);
# 당해 영업중 음식점 view만들기
drop view if exists operate_food;
create view operate_food as
select 개방자치단체코드, year(폐업일자) as 연도,count(*) as 개수,SUBSTRING_INDEX(소재지전체주소, ' ', 2) as 주소
from utf 
where 폐업일자!=''
group by 개방자치단체코드,year(폐업일자),주소
order by 개방자치단체코드,year(폐업일자);
# 영업중인 음식점 view만들기
# 전체 처음부터 해당연도까지 전부를 더하고 폐업을 뺴면 영업중

select * from open_food as o left join close_food as c
on o.연도=c.연도 and o.개방자치단체코드=c.개방자치단체코드;

drop view if exists operate_info;
create view operate_info as
select op1.개방자치단체코드, op1.연도, op1.누적총합, cl1.누적폐업
from
(select 개방자치단체코드, 연도, (select sum(개수) from open_food as o1 where o1.연도<=o2.연도 and o1.개방자치단체코드=o2.개방자치단체코드) as 누적총합 from open_food as o2
group by 개방자치단체코드,연도
order by 개방자치단체코드,연도) as op1 left join
(select 개방자치단체코드, 연도, (select sum(개수) from close_food as o1 where o1.연도<=o2.연도 and o1.개방자치단체코드=o2.개방자치단체코드) as 누적폐업 from close_food as o2
group by 개방자치단체코드,연도
order by 개방자치단체코드,연도) as cl1
on op1.연도=cl1.연도 and op1.개방자치단체코드=cl1.개방자치단체코드 ;

drop view if exists operate_total;
create view operate_total as
select 개방자치단체코드,연도,(ifnull(누적총합,0)-ifnull(누적폐업,0)) as 영업중 from operate_info; 

# 테이블 합치기
# 신생업장 수, 폐업장 수, 영업중 수,폐업률
drop view if exists food;
create view food as
select o1.개방자치단체코드, o1.연도, o1.개수 as 창업, c1.개수 as 폐업, b.영업중 as 영업중,
round((c1.개수/(b.영업중+ifnull(c1.개수,0)))*100,2) as 폐업률,
o1.주소 as 주소
from 
open_food o1 left join close_food c1 
on o1.연도=c1.연도 and o1.개방자치단체코드=c1.개방자치단체코드
left join operate_total b
ON o1.연도 = b.연도
AND o1.개방자치단체코드 = b.개방자치단체코드;
select * from food where 주소 like '%화천군%';





