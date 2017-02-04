from threading import Thread
import time
def sing():
    for i in range(3):
        time.sleep(1)
        print("sing")

def dance():
    for i in range(5):
        time.sleep(1)
        print("dance")
t1 = Thread(target = sing)
t1.start()

t2 = Thread(target = dance)
t2.start()
