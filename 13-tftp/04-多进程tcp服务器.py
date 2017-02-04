# coding=utf-8

from multiprocessing import *
from socket import *

def newSocketDeal(newSocket, destAddr):
     try:
        while True:
            recvData = newSocket.recv(1024)

            if len(recvData) > 0:
                print("revc[%s]: %s"%(str(destAddr), str(recvData)))
                newSocket.send(recvData)
            else:
                print("[%s]客户端先关闭了"%str(destAddr))
                break
     finally:
        newSocket.close()


serverS = socket(AF_INET, SOCK_STREAM)
serverS.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverS.bind(('', 7788))
serverS.listen(2)

while True:
    print("-----主进程，等待客户端访问")
    newSocket, destAddr = serverS.accept()
    print("---主进程，处理数据%s"%str(destAddr))
    newProcess = Process(target=newSocketDeal, args=(newSocket, destAddr))
    newProcess.start()

    newSocket.close()

serverS.close()
