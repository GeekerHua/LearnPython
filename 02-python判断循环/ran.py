import random
computer = random.randint(0,2)
player =  int(input("请输入数字："))
if (player == 0 and computer ==2) or (player == 1 and computer ==0) or (player == 2 and computer == 1):
    print("赢了")
elif player == computer:
    print("平手")
else:
    print("输了")

