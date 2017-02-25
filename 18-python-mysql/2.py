# coding=utf-8
from MysqlHelper import MysqlHelper

sqlHelper = MysqlHelper('localhost', 3306, 'python3', 'root', '1234qwer')

# name = raw_input("Please input student name")
# id1 = raw_input("Please input student id")
#
# # 修改
# sql = 'update students set name=%s where id=%s'
# params = [name, id1]
# sqlHelper.excecute(sql, params)

# sqlHelper.cud(sql, params)


# 查询
sql = 'select * from students where id = 3'
result = sqlHelper.fetchAll(sql, [])
print(result)
