list = [234,346,55,'2.342','sdvsdf','6',98,4.3,4.3,4.3,4.3,4.3]

def digitList(array):
    digitArray = []
    for item in array:
        if type(item) == int or type(item) == float:
            print (item)
            digitArray.append(item)
    digitArray.sort()
    return digitArray

def minNum(array):
    print(digitList(array))
    return digitList(array)[0]

def maxNum(array):
    return digitList(array)[-1]

print("最小值为：%f ,最大值为：%f"%(minNum(list), maxNum(list)))
