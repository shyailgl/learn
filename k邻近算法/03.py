from sklearn.datasets import load_iris, fetch_20newsgroups
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
#
iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

estimator = KNeighborsClassifier()
param_grid = {"n_neighbors": [1, 3, 5, 7]}
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=5)
estimator.fit(x_train, y_train)
y_pre = estimator.predict(x_test)
print("预测值是：\n", y_pre)
print("预测值和真实值的对比是：\n", y_pre == y_test)
score = estimator.score(x_test, y_test)
print("准确率为：\n", score)

# 查看交叉验证网络搜索的一些参数
print("在交叉验证中，得到最好的结果是：\n", estimator.best_score_)
print("在交叉验证中，得到最好的模型是：\n", estimator.best_estimator_)
print("在交叉验证中，得到的模型结果是：\n", estimator.cv_results_)
