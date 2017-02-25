# coding=utf-8

from socket import *
import re
from multiprocessing import *


def handleRequest(newSocket):
    recvData = newSocket.recv(1024)
    # 匹配GET
    if recvData.startswith("GET"):
        print("收到请求\n%s\n" % (recvData))

        result = re.match(r'GET /([^ ]*)', recvData)
        path = result.group(1)
        if path == '':
            path = 'index.html'

        try:
            f = open(path)
        except:
            responseData = 'HTTP1.1 404 Not Found\r\n'
            responseData += '\r\n'
            responseData += '文件未找到'
        else:
            responseData = 'HTTP1.1 200 OK\r\n'
            responseData += '\r\n'
            responseData += f.read()
        finally:
            newSocket.send(responseData)
            newSocket.close()
            f.close()

    else:
        return 'HTTP1.1 404 Not Found'


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', 7780))
serverSocket.listen(4)


while True:
    newSocket, destAddr = serverSocket.accept()
    p = Process(target=handleRequest, args=(newSocket,))
    p.start()
    newSocket.close()

serverSocket.close()
