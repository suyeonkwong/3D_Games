import pymysql

class DaoExam:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='mypydb', charset='utf8')
        self.curs = self.conn.cursor()
        
    def insert(self,exam_id,e_id,kor,eng,mat):
        sql = f"""
        insert into exam
         (e_id,kor,eng,mat,in_user_id,in_date,up_user_id,up_date)
        values ('{e_id}','{kor}','{eng}','{mat}','1',DATE_FORMAT(NOW(), '%Y%m%d%H%m%s'),'1',DATE_FORMAT(NOW(), '%Y%m%d%H%m%s'))"""
        
        print(sql)
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def delete(self,exam_id):
        sql = "DELETE FROM exam WHERE exam_id=%s"
        val = (exam_id)
        
        print(sql)
        self.curs.execute(sql,val)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def update(self,exam_id,e_id,kor,eng,mat):
        sql = "update exam set e_id=%s, kor=%s, eng=%s, mat=%s where exam_id=%s"
        val = (e_id, kor, eng, mat, exam_id)
        
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
            exam_id,
            e_id,
            kor,
            eng,
            mat,
            in_user_id,
            in_date,
            up_user_id,
            up_date
        from exam
        """
        
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            ret.append({'exam_id':row[0], 'e_id':row[1], 'kor':row[2], 'eng':row[3], 'mat':row[4]
                        , 'in_user_id':row[5], 'in_date':row[6], 'up_user_id':row[7], 'up_date':row[8]})
        return ret
        
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoExam()
    arr = de.selectlist();
    print(arr)
