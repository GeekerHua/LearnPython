import os

pid =  os.fork()

if pid == 0:
    while True:
        print("hello")
elif pid > 0:
    while True:
        print("mac")
