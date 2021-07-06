import pymysql
 
class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(
            user="root",
            password="python",
            host="127.0.0.1",
            port=3306,
            database="mypydb"
        )
        self.curs = self.conn.cursor()
    
    def get_prices(self,c_name):    
        
        ret = []
        sql = f"""select s_code,c_name,price,crw_date from stock where c_name='{c_name}'"""
        #print(sql)
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            ret.append(row[2])
        return ret
        
    def get_name(self):
        
        ret = []
        sql = "select c_name from stock group by c_name"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for i in rows:
            ret.append(i[0])
        #print(ret)
        return ret
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    ds = DaoStock()
    list = ds.get_prices("삼성전자")
    #print(list)
    #ds.get_name()
    
   