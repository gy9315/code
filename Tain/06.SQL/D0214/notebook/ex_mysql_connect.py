import pandas as pd
import pymysql as pl
conn=pl.connect(host='localhost',user='root',password='1234',db='sakila')
cur=conn.cursor(pl.cursors.DictCursor)
cur.execute('select * from language ')
desc=cur.description
for x in cur:
    print(x)
rows=cur.fetchall()
# print(rows) 
# DF=pd.DataFrame(rows)
# print(DF)