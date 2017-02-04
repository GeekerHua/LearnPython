score = int(input("请输入当前分数："))
guize = int(input("请输入违反了哪项交通规则(1:闯红灯，2:违章停车)"))
if guize == 1:
    score -= 6
if guize == 2:
    score -= 3

if score > 0:
    print("当前分数为%d,不需要进行学习"%score)
else:
    print("当前分数为%d,需要进行学习"%score)
