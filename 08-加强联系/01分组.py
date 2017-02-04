list1 = range(1,101)
list2 = [x for x in range(1,101)]

list3 = [[list[i], list[i+1], list[i+2]] for i in range(0,len(list)) if i%3 ==0 ]
