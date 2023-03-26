import pandas as pd
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
         'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
         'Normal Nucleoli', 'Mitoses', 'Class']

data = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
    names=names)
print(data)
data = data.replace(to_replace="?", value=np.nan)
data = data.dropna()
x = data.iloc[:, 1:-1]
y = data["Class"]

# 分割数据
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)
# 标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)
estimator = LogisticRegression()
estimator.fit(x_train, y_train)
ret = estimator.score(x_test, y_test)
print("准确率为：\n", ret)
y_pre = estimator.predict(x_test)
print("预测值为：\n", y_pre)
# 精确率召回率
ret = classification_report(y_test, y_pre, labels=(2, 4), target_names=('良性', '恶性'))
print(ret)
# roc曲线与auc指标
# 必须在[0-1]
y_test = np.where(y_test > 3, 1, 0)
print(roc_auc_score(y_test, y_pre))
