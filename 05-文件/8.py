count = int(input("请输入需要打印的行数："))

def draw(count):
    i= 0

    while i < count:
        j = 0
        while j <= i:
            print("*",end = '')
            j += 1
        print("")
        i += 1

draw(count)
