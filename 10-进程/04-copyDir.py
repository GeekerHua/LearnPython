#coding=utf-8
import os ,time
from multiprocessing import Process
from multiprocessing import Pool
from Queue import Queue

def copyItem(fileName, q):
    f = open(fileName, 'r')
    newFile = open(('copy/' + fileName), 'w')

    print('哈哈')
    for line in f.readlines():
        newFile.write(line)
        print("line")
    f.close()
    newFile.close()
    q.put(fileName)

# 拷贝当前文件夹
q = Queue(3)
files = os.listdir()
os.mkdir('copy')
po = Pool(3)
for f in files:
    po.apply_async(copyItem, (f, q))
    #copyItem(f)
'''
allFilesNum = len(files)
for i in range(allFilesNum):
    name= q.get()
    print("%f----%s"%((i/allFilesNum), name))
'''
po.close()
po.join()

