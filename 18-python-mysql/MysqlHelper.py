# coding=utf-8
from MySQLdb import *

class MysqlHelper:
    def __init__(self, host, port, db, user, passwd, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.coon = connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd, charset=self.charset)
        self.cursor = self.coon.cursor()

    def close(self):
        self.cursor.close()
        self.coon.close()

    # 闭包
    def __execute(func):
        def wrappedfunc(self, sql, params):
            try:
                self.open()
                self.cursor.execute(sql, params)
                result = func(self, sql, params)
                self.close()
                return result
            except Exception, e:
                print(e)
        return wrappedfunc

    @__execute
    def fetchOne(self, sql, params):
        return self.cursor.fetchone()

    @__execute
    def fetchAll(self, sql, params):
        return self.cursor.fetchall()

    @__execute
    def excecute(self, sql, params):
        self.coon.commit()



