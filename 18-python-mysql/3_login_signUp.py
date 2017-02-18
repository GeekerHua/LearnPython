# coding=utf-8

from  MysqlHelper import  MysqlHelper
from hashlib import sha1

# passwd
def encryption(passwd):
    s1 = sha1()
    s1.update(passwd)
    pw2 = s1.hexdigest()
    return pw2


def login():
    name = raw_input('Please input user name:')
    pwd = raw_input('Please input user password:')
    hashPwd = encryption(pwd)

    sql = 'select passwd from users where name=%s'
    result = sqlHelp.fetchOne(sql, [name])
    if result == None:
        print("Not have this name!!!")
    elif result[0] == hashPwd:
        print("login success")
    else:
        print("login faild, Error name or password!!!")


def signUp():
    name = raw_input('Please input user name:')
    pwd = raw_input('Please input user password:')
    hashPwd = encryption(pwd)

    sql = 'select name from users where name=%s'
    result = sqlHelp.fetchOne(sql, [name])
    if result != None:
         print("There has the same name, please change a new name.")
    else:
        newSql = 'insert into users VALUES(0, %s, %s)'
        sqlHelp.excecute(newSql, [name, hashPwd])
        print('signUp success')

if __name__ == "__main__":
    sqlHelp = MysqlHelper('localhost', 3306, 'python3', 'root', '1234qwer')

    inputStr = raw_input("1:login, 2:sign up  >> ")
    if inputStr == "1":
        login()
    elif inputStr == "2":
        signUp()
    else:
        print("Please input right key")
