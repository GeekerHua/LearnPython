li = [13,24346,5457,65687,8,121,12,658879]
maxNum = li[0]
minNum = li[0]
for num in li:
    if num > maxNum:
        maxNum = num
    elif num < minNum:
        minNum = num
print("最大值为：%d，最小值为： %d"%(maxNum,minNum))
