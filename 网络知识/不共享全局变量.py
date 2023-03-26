import multiprocessing
import os

# 全局遍量
my_list = []


# 写入数据
def write_data():
    for i in range(3):
        my_list.append(i)
        print("add:", i)
    print(my_list)


def read_data():
    print(my_list)


if __name__ == '__main__':
    # 创建写入数据进程
    write_process = multiprocessing.Process(target=write_data)
    # 创建读取数据进程
    read_process = multiprocessing.Process(target=read_data)
    write_process.start()
    read_process.start()