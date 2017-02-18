# coding=utf-8

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', 7788))

serverSocket.listen(4)

while True:
    newSocket, destAddr = serverSocket.accept()

    print("处理数据 ip = %s" % str(destAddr))
    try:
        while True:
            recvData = newSocket.recv(1024)

            if len(recvData) > 0:
                print("处理消息%s" % recvData)
            else:
                print("客户端先关闭了")
                break
    finally:
        newSocket.close()
serverSocket.close()
