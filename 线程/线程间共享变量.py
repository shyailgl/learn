import threading

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
    write_thread = threading.Thread(target=write_data)
    read_thread = threading.Thread(target=read_data)
    write_thread.start()
    read_thread.start()
