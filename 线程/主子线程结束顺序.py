# 编写代码
import time
import threading


def coding(num):
    for i in range(num):
        print("coding.....")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程
    coding_thread = threading.Thread(target=coding, args=(10,), daemon=True)
    # coding_thread.setDaemon(True)
    coding_thread.start()
    time.sleep(1)
    print("主线程执行完毕")
