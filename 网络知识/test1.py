import time
import multiprocessing
import os


def coding(num, name):
    print(os.getpid())
    print("父进程------%d"% os.getppid())
    for i in range(num):
        print(name)
        print("coding .....")
        time.sleep(0.2)


def music(count):
    print(os.getpid())
    print("父进程------》%d"%os.getppid())
    for i in range(count):
        print("music .....")
        time.sleep(0.5)


if __name__ == '__main__':
    # coding()
    # music()
    print("主进程------》%d"%os.getppid())
    coding_process = multiprocessing.Process(target=coding, args=(3, "你好"))
    print("主进程------》%d"%os.getppid())
    music_process = multiprocessing.Process(target=music, kwargs={"count": 3})
    coding_process.start()
    music_process.start()
