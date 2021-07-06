import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='mypydb', charset='utf8')
 
curs = conn.cursor()
 
sql = "insert into sampk (row02,row03) values (%s,%s)"
val = ("3", "3")
curs.execute(sql,val)
conn.commit()
cnt = curs.rowcount

print("cnt",cnt)

conn.close()