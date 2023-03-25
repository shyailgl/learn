from sklearn.datasets import load_iris, fetch_20newsgroups
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
#
iris = load_iris()
# print(iris)
#
# news=fetch_20newsgroups()
# print(news)
iris_d = pd.DataFrame(data=iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
iris_d["target"] = iris.target


def iris_plot(data, col1, col2):
    sns.lmplot(x=col1, y=col2, data=data, hue="target", fit_reg=False)
    plt.title('英伟华数据显示')
    plt.show()


# iris_plot(iris_d,'Sepal_Width','Petal_Length')
# iris_plot(iris_d,'Sepal_Length','Petal_Width')
# print(iris_d)
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
print("训练集的特征值：\n", x_train)
print("训练集的目标值：\n", y_train)
print("测试集的特征值：\n", x_test)
print("测试集的目标值：\n", y_test)
x_train1, x_test1, y_train1, y_test1 = train_test_split(iris.data, iris.target, test_size=0.2, random_state=2)
x_train2, x_test2, y_train2, y_test2 = train_test_split(iris.data, iris.target, test_size=0.2, random_state=2)
print("训练集的目标值：\n", y_test)
print("训练集的目标值：\n", y_test1)
print("训练集的目标值：\n", y_test2)
