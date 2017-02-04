import os
files = os.listdir()

for fileName in files:
    os.rename(fileName, fileName[fileName.find('华少出品，必属精品'):])

