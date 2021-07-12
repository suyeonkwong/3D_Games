import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='mypydb', charset='utf8')
        self.curs = self.conn.cursor()
        
    def insert(self,e_id,e_name,tel,address):
        sql = f"""
        insert into emp
         (e_name,tel,address,in_user_id,in_date,up_user_id,up_date)
        values ('{e_name}','{tel}','{address}','1',DATE_FORMAT(NOW(), '%Y%m%d%H%m%s'),'1',DATE_FORMAT(NOW(), '%Y%m%d%H%m%s'))"""
        
        print(sql)
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def delete(self,e_id):
        sql = "DELETE FROM emp WHERE e_id=%s"
        val = (e_id)
        
        print(sql)
        self.curs.execute(sql,val)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def update(self,e_name,tel,address,e_id):
        sql = "update emp set e_name=%s,tel=%s, address=%s where e_id=%s"
        val = (e_name, tel, address, e_id)
        
        print(sql)
        print(val)
        self.curs.execute(sql,val)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
        
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
