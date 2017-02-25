# coding=utf-8

from socket import *
import re
from multiprocessing import *


def handleRequest(newSocket):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
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
                    content = f.read()
                    responseData = 'HTTP1.1 200 OK\r\n'
                    responseData += 'Content-Length: %d' % len(content)
                    responseData += '\r\n'
                    responseData += content
                finally:
                    newSocket.send(responseData)
                    f.close()
            else:
                return 'HTTP1.1 404 Not Found'
        else:
            newSocket.close()


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
