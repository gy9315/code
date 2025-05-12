import pandas as pd
import pymysql as pl
conn=pl.connect(host='localhost',user='root',password='1234',db='sakila')
cur=conn.cursor(pl.cursors.DictCursor)
# count=0
# for x in cur:
#     if count==0:
#         print(x.keys())
#     count+=1
# rows=cur.fetchall()
sql1='''
drop table if exists customer1;
'''
sql2='''
create table customer1
(name varchar(20),
category varchar(4),
region varchar(20))'''
sql3='''
insert into customer1(name,category,region)
values
(%s,%s,%s)
'''
list1=(('홍길동',1,'서울'),('이연수',2,'서울'))
cur.execute(sql1)
cur.execute(sql2)
cur.executemany(sql3,list1)
cur.execute('select * from customer1')
conn.commit()
row=cur.fetchall()
print(row)

cur.close()
conn.close()