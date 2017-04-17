import sqlite3

coon = sqlite3.connect('spider.db')
cu = coon.cursor()
coon.execute("insert into T_PROXY values(?, ?, ?)",
             ('192.21.4.56', '8080', 'HTTP'))
coon.commit()
# if cu is not None:
# cu.close()
coon.close()
