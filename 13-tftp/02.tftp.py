#coding=utf-8
from socket import *
import struct
def sendRequest(string):
    l = len(string)
    nameStr = ("!H%dsb5sb"%l)
    return struct.pack(nameStr, 1, string, 0, "octet", 0)

def sendAck(code):
    nameStr = ("!HH")
    return struct.pack(nameStr, 4, code)

def recv(f):
    recvData, recvAddr = csocket.recvfrom(516)

    f.write(recvData[4:])

    ackCode = struct.unpack("!HH",recvData[:4])[1]
    csocket.sendto(sendAck(ackCode), recvAddr)

    print("\r已接收第%d个数据包"%(ackCode)),

    if len(recvData) != 516:
        print("\n全都收完了***********")
        f.close()
        return True


fileName = 'test.png'
csocket = socket(AF_INET, SOCK_DGRAM)
csocket.sendto(sendRequest(fileName), ("192.168.17.89", 69))
f = open(fileName, "w")

while True:
    resultStatus = recv(f)
    if resultStatus:
        break




