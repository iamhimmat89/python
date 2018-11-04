from time import *
from threading import *

print("start")


class ThreadHello(Thread):
    def run(self):
        for i in range(5):
            sleep(0.2)
            print("Hello")


class ThreadHi(Thread):
    def run(self):
        for i in range(5):
            sleep(0.2)
            print("Hi")


thread_1 = ThreadHello()
thread_2 = ThreadHi()

thread_1.start()
sleep(0.2)
thread_2.start()

thread_1.join()
thread_2.join()

print("end")
