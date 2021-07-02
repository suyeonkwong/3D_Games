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

sql = "UPDATE sampk SET row02='바보', row03='멍청이' WHERE row01='5'"

cur.execute(sql)

conn.commit()

print(cur.rowcount, "record")

