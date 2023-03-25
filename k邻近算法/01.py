from sklearn.neighbors import KNeighborsClassifier

# 构造数据
x = [[1], [2], [10], [20]]
y = [0, 0, 1, 1]
# 模型训练
estimator = KNeighborsClassifier(n_neighbors=1)
#
estimator.fit(x, y)
# 数据预测
ret = estimator.predict([[0]])
print(ret)
ret1 = estimator.predict([[100]])
print(ret1)
