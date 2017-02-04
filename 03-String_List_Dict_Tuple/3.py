
paths = []
while True:
    path = input("请输入路径,按0结束输入")
    if path == "0":
        p = '/'
        p = '/' + p.join(paths)
        print(p)
        break
    else:
        paths.append(path)

