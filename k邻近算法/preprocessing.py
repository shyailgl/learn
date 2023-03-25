import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def minmax_demo():
    data = pd.read_csv("../data/dating.txt")
    print(data)


minmax_demo()
