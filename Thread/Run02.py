"""
加锁等待线程结束
"""

import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

# n个线程需要暂停的时间
loops = [2, 4, 5, 7]


def loop(nloop, nsec, lock):
    logging.info("start " + str(nloop) + " at" + ctime())
    sleep(nsec)
    logging.info("end " + str(nloop) + " at" + ctime())
    # 释放锁
    lock.release()


def main():
    logging.info("satrt all at" + ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        # 声明一个锁
        lock = _thread.allocate_lock()
        # 锁上
        lock.acquire()
        # 将锁加入到锁池中
        locks.append(lock)

    # 开启线程
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    # 死循环判断所有的锁是否锁住，锁住就一直循环，没锁了就退出
    for i in nloops:
        while locks[i].locked():
            pass
    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()
