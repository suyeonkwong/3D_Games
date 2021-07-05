import requests
from bs4 import BeautifulSoup
import mariadb
import sys
from sqlalchemy.sql.functions import now
from _datetime import datetime
from time import strftime
url = 'https://vip.mk.co.kr/newSt/rate/item_all.php'

response = requests.get(url)
response.encoding='euc-kr'

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

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    #code = soup.select('a[title='*']')
    price = soup.select('.st2 + td')
    name = soup.select('.st2 > a')
    
    for i in range(len(price)):
        #print(name[i].attrs["title"], name[i].text, int(price[i].text.replace(",", "")))
        sql = "INSERT INTO stock (s_code, s_name, price, crw_date) VALUES (%s, %s, %s, %s)"
        val = (name[i].attrs["title"], name[i].text, int(price[i].text.replace(",", "")), datetime.now().strftime('%Y%m%d.%H%M'))
        cur.execute(sql, val)

    conn.commit()

    print(cur.rowcount, "record inserted")

else : 
    print(response.status_code)
    

    
    
