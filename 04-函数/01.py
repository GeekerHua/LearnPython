def sum2num(num1,num2):
    print(num1 +  num2)

num1 = input("请输入第一个数： ")
num2 = input("请输入第二个数： ")
if num1.isdigit() and num2.isdigit():
    sum2num(int(num1), int(num2))
else:
    print("请输入纯数字")
