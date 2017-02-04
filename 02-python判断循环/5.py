i = 0
while i <= 8:
    j = 0
    if i < 5:
        while j <= i:
            print ("* ",end = "")
            j += 1
    else:
        while j <=( 8 - i):
            print ("* ",end = "")
            j += 1
    print("")
    i += 1
