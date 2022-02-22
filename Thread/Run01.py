"""
硬性等待线程结束
"""

import _thread
import logging
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)

def loop01():
    logging.info("start loop01 at" + ctime())
    sleep(4)
    logging.info("end loop01 at" + ctime())

def loop02():
    logging.info("start loop02 at" + ctime())
    sleep(2)
    logging.info("end loop02 at" + ctime())

def main():
    logging.info("satrt all at" + ctime())
    # 添加子线程
    _thread.start_new_thread(loop01,())
    _thread.start_new_thread(loop02,())
    # _thread 会在主线程结束时强制kill子线程，所以要将主线程停6S
    sleep(6)
    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()
