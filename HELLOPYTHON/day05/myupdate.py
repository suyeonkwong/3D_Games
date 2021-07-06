import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='mypydb', charset='utf8')
 
curs = conn.cursor()
 
sql = "update sampk set row02=%s,row03=%s where row01=%s"
val = ("4", "4","3")
curs.execute(sql,val)
conn.commit()
cnt = curs.rowcount

print("cnt",cnt)

conn.close()