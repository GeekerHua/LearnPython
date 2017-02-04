from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("", 7788))
udpSocket.sendto('hello\n', ("192.168.17.54", 8080))

recveData = udpSocket.recvfrom(1024)
print(recveData)


udpSocket.close()
