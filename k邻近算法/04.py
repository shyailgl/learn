from sklearn.datasets import load_iris, fetch_20newsgroups
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("../data/FBlocation/train.csv")
# test=pd.read_csv("../data/FBlocation/test.csv")
# print(data.head())
# 1.获取数据集
# 2.基本数据处理
# 3.缩小数据范围
# 4.选择时间特征
# 5.去掉签到较少的地方
# 6.确定特征值和目标值
# 7.分割数据集
# 8.特征工程
# 9.机器学习
# 10.模型评估
# print(data.shape)
# data.describe()
partial_data = data.query("x > 2.0 & x < 2.5 & y > 2.0 & y < 2.5")
# partial_data["time"].head()
time = pd.to_datetime(partial_data["time"], unit="s")
time = pd.DatetimeIndex(time)
partial_data["hour"] = time.hour
partial_data["day"] = time.day
partial_data["weekday"] = time.weekday
place_count = partial_data.groupby("place_id").count()

place_count = place_count[place_count["row_id"] > 3]
print(place_count.head())
partial_data = partial_data[partial_data["place_id"].isin(place_count.index)]
x = partial_data[["x", "y", "accuracy", "hour", "day", "weekday"]]
y = partial_data["place_id"]
# print(x.head())
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size=0.25)
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)
estimator = KNeighborsClassifier()
param_grid = {"n_neighbors": [3, 5, 7, 9]}
estimator = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=3, n_jobs=-1)
estimator.fit(x_train, y_train)
score_ret=estimator.score(x_test,y_test)
print("准确率为：\n", score_ret)

