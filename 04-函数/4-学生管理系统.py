#!/usr/bin/env python
# coding=utf-8

stuList = []
tmpInfo = ()

def printMenu():
    list = ["   学生管理系统v2.6", "1:添加学生信息", "2:删除学生信息", "3:修改学生信息", "4:查询学生信息", "5:显示所有学生", "0:退出系统"]
    print("*"*50)
    for str in list:
        print(str)
    print("*"*50)

def getStudentInfo():

    global tmpInfo
    name = input("请输入姓名:")
    sex = input("请输入性别:")
    age = input("请输入年龄:")
    tmpInfo = (name, sex, age)

def addStudent():
    getStudentInfo()
    stuList.append({'name': tmpInfo[0], 'sex': tmpInfo[1], 'age': tmpInfo[2]})


def removeStudent():
    no = input("请输入需要删除的学生序号：")
    if no.isdigit() and int(no) <= len(stuList):
        del stuList[int(no) - 1]
        print("删除成功")
    else:
        print("指令不合")

def modifyStudent():
    getStudentInfo()

    no = input("请输入需要删除的学生序号：")
    stuList[no -1] = {'name': tmpInfo[0], 'sex': tmpInfo[1], 'age': tmpInfo[2]}
    print("修改完成")


def searchStudent():
    name = input("请输入你要搜索的姓名:")
    for stu in stuList:
        if stu['name'] == name:
            print("^"*50)
            print(" %s        %s        %s"%(stu['name'], stu['sex'], stu['age']))




def showAll():
    print("序号    姓名    性别    年龄")
    print("="*50)
    no = 1
    for stu in stuList:
        print("%d        %s        %s        %s"%(no, stu['name'], stu['sex'], stu['age']))
        no += 1

def main():
    while True:
        printMenu()
        select =input("请输入指令：")

        if select == "1":
            addStudent()
        elif select == '2':
            removeStudent()
        elif select == "3":
            modifyStudent()
        elif select == '4':
            searchStudent()
        elif select == '5':
            showAll()
        elif select == "0":
            exit()
        else:
            print("指令不合法，请重新输入")
            break
main()
