import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="python",
        host="127.0.0.1",
        port=3306,
        database="mypydb"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

# selectall = "SELECT * from employee" 
sql = "SELECT row01, row02, row03 from sampk" 
cur.execute( sql )

# query 결과를 list 형으로 가져옴.
resultset = cur.fetchall()

for row01, row02, row03,  in resultset: 
    print(f"row01: {row01}, row02: {row02}, row03: {row03} ")