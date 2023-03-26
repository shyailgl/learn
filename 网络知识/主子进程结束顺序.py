import multiprocessing
import os
import time


# 工作函数
def work():
    for i in range(10):
        print("工作中。。。。")
        time.sleep(0.2)


if __name__ == '__main__':
    #     创建子进程
    work_process = multiprocessing.Process(target=work)
    # work_process.daemon=True
    work_process.start()
    time.sleep(1)
    work_process.terminate()
    print("主进程执行完毕")
