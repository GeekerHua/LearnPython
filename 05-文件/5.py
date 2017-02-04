import os
files = os.listdir()

for fileName in files:
    os.rename(fileName, '华少出品，必属精品' + fileName)

