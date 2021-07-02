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

sql = "delete from sampk where row01='1'"

cur.execute(sql)

conn.commit()

print(cur.rowcount, "record")