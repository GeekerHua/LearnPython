#coding=utf-8
from socket import *
import time

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("", 7788))
udpSocket.sendto('hello\n', ("192.168.17.54", 8080))

while True:
    recvData = udpSocket.recvfrom(1024)
    print("[%s] %s:%s"%(time.ctime(), recvData[1][0], recvData[0]))

