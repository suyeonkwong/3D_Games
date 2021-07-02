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

#row01 = 3
#row02 = "3"
#row03 = "3"
#
#insert_query = "INSERT INTO sampk (row01,row02,row03) VALUES (?, ?, ?)"
#
#try: 
#    cur.execute( insert_query, (row01, row02, row03))
#except mariadb.Error as e: 
#    print(f"Error: {e}")

sql = "INSERT INTO sampk (row02, row03) VALUES (%s, %s)"
val = ("3", "3")

cur.execute(sql, val)

conn.commit()

print(cur.rowcount, "record inserted")
