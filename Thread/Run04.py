"""
继承Thread，调用init方法，重写run方法
"""
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

# n个线程需要暂停的时间
loops = [2, 4, 5, 7]
class MyThread(threading.Thread):
    def __init__(self,func,args=()):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        # self.name = name

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    logging.info("start " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end " + str(nloop) + " at " + ctime())


def main():
    logging.info("satrt all at" + ctime())
    threads = []
    nloops = range(len(loops))

    # 开启线程
    for i in nloops:
        threadName ="第" + str(i+1) + "个线程"
        t = MyThread(loop,(threadName,loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()
