#!E:\python2.7\python.exe
# -*- coding: UTF-8 -*-


print                               # 空行，告诉服务器结束头部
import MySQLdb


class WebSiteDB:

    tableName="news"

    def __init__(self, dbname = 'he', hostname = '127.0.0.1', username = 'root', password = 'root'):
        self.dbname = dbname
        self.hostname = hostname
        self.username = username
        self.password = password
        
        self.conn = None
        self.cursor = None
        self.__connectMySql()
        

    def __connectMySql(self):
        try:
            self.conn = MySQLdb.connect(self.hostname, self.username, self.password, self.dbname,charset='GBK')
            self.cursor = self.conn.cursor()
        except:
            print 'fail to connect to MySQLdb '

   

    def fetchOne(self,tablename):
      
      
        try:
            self.cursor.execute('select * from ' + tablename)
            result = self.cursor.fetchone()
            return result
        except:
            print 'fail to fetchOne'
            return None

    def fetchAll(self, tablename):
        try:
            self.cursor.execute('select * from ' + tablename)
            results = self.cursor.fetchall()
            return results
        except:
            print 'fail to fetchAll'
            return None
    
    def insertOneRd(self,sql):
            self.cursor.execute(sql)
            self.conn.commit()
        
    

                                                 