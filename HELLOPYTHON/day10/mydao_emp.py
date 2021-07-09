import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='mypydb', charset='utf8')
        self.curs = self.conn.cursor()
        
    def insert(self):
        return 1
        
    def selectlist(self):
        ret = []
        sql = """
        select
            e_id,
            e_name,
            tel,
            address,
            in_user_id,
            in_date,
            up_user_id,
            up_date
        from emp
        """
        
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            ret.append({'e_id':row[0], 'e_name':row[1], 'tel':row[2], 'address':row[3]
                        , 'in_user_id':row[4], 'in_date':row[5], 'up_user_id':row[6], 'up_date':row[7]})
        return ret
        
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    arr = de.selectlist();
    print(arr)
