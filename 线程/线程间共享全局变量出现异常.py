import threading

g_num=0

def sum_num1():
    for i in range(1000000):
        global  g_num
        g_num+=1
    print("g_num1",g_num)
def sum_num2():
    for i in range(1000000):
        global  g_num
        g_num+=1
    print("g_num2",g_num)

if __name__ == '__main__':
    sum1_thread=threading.Thread(target=sum_num1)
    sum2_thread=threading.Thread(target=sum_num2)
    sum1_thread.start()
    sum2_thread.start()


