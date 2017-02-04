def sum(begin,n):
    if n > begin:
        return  n+sum(begin,n -1)
    else:
        return begin
print(sum(100,200))
