# 编写代码
import time
import threading

def coding(num):
    for i in range(num):
        print("coding.....")
        time.sleep(0.2)


def music(num):
    for i in range(num):
        print("music....")
        time.sleep(0.2)


if __name__ == '__main__':
    # coding()
    # music()
    # 创建子线程
    coding_thread=threading.Thread(target=coding,args=(3,))
    music_thread=threading.Thread(target=music,kwargs={"num":3})
    coding_thread.start()
    music_thread.start()
