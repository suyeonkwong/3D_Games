import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='mypydb', charset='utf8')
 
curs = conn.cursor()
 
sql = "select * from sampk"
curs.execute(sql)
 
rows = curs.fetchall()
print(rows)     

conn.close()

#for row01, row02, row03,  in resultset: 
#    print(f"row01: {row01}, row02: {row02}, row03: {row03} ")