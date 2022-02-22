"""
使用threading
"""
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

# n个线程需要暂停的时间
loops = [2, 4, 5, 7]

def loop(nloop, nsec):
    logging.info("start " + str(nloop) + " at" + ctime())
    sleep(nsec)
    logging.info("end " + str(nloop) + " at" + ctime())


def main():
    logging.info("satrt all at" + ctime())
    threads = []
    nloops = range(len(loops))

    # 开启线程
    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        # 一个子线程还没结束就会一直阻塞主线程，直至子线程结束
        threads[i].join()
    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()
