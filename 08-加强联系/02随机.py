import random
n = 10

def test3():
    li = []
    while True:
        x = random.randint(1,n)
        if x not in li:
            li.append(x)
            if len(li) == n:
                print(li)
                break


test3()
