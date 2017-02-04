from multiprocessing import Process
import time
def dance():
    while True:
        print("dance")
        time.sleep(1)
def sing():
    while True:
        print("sing")
        time.sleep(1)

p1 = Process(target = dance)
p2 = Process(target = sing)

p1.start()
p2.start()

