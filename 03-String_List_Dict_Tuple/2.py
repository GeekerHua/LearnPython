word = 'hello world'
wList = []
for w in word:
    if w not in wList and w != ' ':
        print("%s:%d "%(w, word.count(w)), end = "")
        wList.append(w)

