from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error


def liner_model1():
    boston = load_boston()
    print(boston)
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)
    print("这个模型的偏执是：\n", estimator.intercept_)
    print("这个模型的系数是：\n", estimator.coef_)
    y_pre = estimator.predict(x_test)
    print("预测值是\n", y_pre)
    #     均方误差
    ret = mean_squared_error(y_test, y_pre)
    print("均方误差：\n", ret)