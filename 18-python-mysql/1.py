# coding=utf-8
#
# """
# # Author = GeekerHua
# # 2017.02.17 10:39:07
# """

from MySQLdb import *

try:
    coon = connect(host='localhost', port=3306, user='root', passwd='1234qwer', db='python3', charset='utf8')
    cursor1 = coon.cursor()

    # sql = "insert into students(name) values('xiaoming')"
    sql = "select * from students"
    cursor1.execute(sql)
    # print(cursor1)
    coon.commit()
    result = cursor1.fetchone()
    print(result[1])

    result2 = cursor1.fetchall()
    print(result2)

    cursor1.close()
    coon.close()
    # print("哈哈")
except Exception, e:
    print(e.message)
