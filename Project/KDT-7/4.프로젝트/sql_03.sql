# retaurant_statics
# primary 키 개방자치단체코드
# close_food primary 키 and 왜래키 개방자치단체코드
# open_food primary 키 and 왜래키 개방자치단체코드
# operate_info primary 키 and 왜래키 개방자치단체코드
# operate_total primary 키 and 왜래키 개방자치단체코드
# food
-- open_food.개방자치단체코드, open_food 연도, open.food 개수 as 창업, close 개수 as 폐업, operate_total 영업중 as 영업중,
-- round((c1.개수/(b.영업중+ifnull(c1.개수,0)))*100,2) as 폐업률,
-- open_food as 주소
# army_grdp restaurant statics 주소 참조
use economic_condition;
alter table restaurant_statics add primary key (번호) ;
alter table army_grdp add primary key (number);
alter table army_grdp add foreign key (주소) references restaurant_statics(소재지전체주소);