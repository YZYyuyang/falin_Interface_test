import pymysql

class MySQLDb(object):

    # 构造方法（实例化时初始调用的方法）
    def __init__(self,database='imlaw'):            #database = '数据库名称'     在此指定数据库名称
        self.db = pymysql.connect(host='121.41.201.151:13306', port='13306',user='yoctech', password='B5Z7P4JOL2M5tIa9', database=database, charset='utf8')
        self.cursor = self.db.cursor()

    def query_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def query_all(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print(result)
        return str(result)

    def update_data(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        #self.db.rollback()

    # 析构方法（收尾工作），什么时候收尾：Python高兴的时候
    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == "__main__":
    mysql = MySQLDb()
    mysql.query_all(sql="select * from article where id = 1")

