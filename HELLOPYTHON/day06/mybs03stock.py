import requests
from bs4 import BeautifulSoup
import mariadb
import sys
from sqlalchemy.sql.functions import now
from _datetime import datetime
from time import strftime, sleep
import time
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

def insertStock(s_code, c_name, price, crw_date):

    sql = "INSERT INTO stock (s_code, c_name, price, crw_date) VALUES (%s, %s, %s, %s)"
    val = (s_code, c_name, price, crw_date)
    
    cur.execute(sql, val)
    
    conn.commit()
    

for i in range(6):

    yyyy = datetime.today().strftime("%Y%m%d.%H%M")
    
    URL = 'https://vip.mk.co.kr/newSt/rate/item_all.php' 
    response = requests.get(URL) 
    response.encoding='euc-kr'
    html = response.text
    
    
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.select(".st2")
    
    
    
    for idx,td in enumerate(tds):
        c_name = td.select_one("a").text
        s_code = td.select_one("a")["title"]
        price = td.parent.select("td")[1].text.replace(",","")
        print(td.parent.select("td")[1].text.replace(",",""))
        insertStock(s_code,c_name,price,yyyy)
    
    sleep(60)


conn.close()
        
        
    #    for i in range(len(price)):
            #print(name[i].attrs["title"], name[i].text, int(price[i].text.replace(",", "")))
    #        sql = "INSERT INTO stock (s_code, s_name, price, crw_date) VALUES (%s, %s, %s, %s)"
    #        val = (name[i].attrs["title"], name[i].text, int(price[i].text.replace(",", "")), datetime.now().strftime('%Y%m%d.%H%M'))
    #        cur.execute(sql, val)
    
    #    conn.commit()
    
    #    print(cur.rowcount, "record inserted")
    
   
    

    
    
