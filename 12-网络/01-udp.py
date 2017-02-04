from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    udpSocket.sendto('hello\n', ("192.168.17.73", 8080))

udpSocket.close()
