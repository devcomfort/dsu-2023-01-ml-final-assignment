"""
https://www.kaggle.com/datasets/hussainnasirkhan/multiple-linear-regression-dataset?resource=download
"""

from sklearn.linear_model import LinearRegression
import pandas as pd
from mpl_toolkits.mplot3d.axes3d import Axes3D
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from random import randint

datasets = pd.read_csv("multiple_linear_regression_dataset.csv")

# sns.pairplot(datasets)
plt.show()

X = datasets[['age', 'experience']]
Y = datasets['income']

reg = LinearRegression().fit(X, Y)

print(reg.predict([(20, 5)]))

print(f"coefficient = {reg.coef_}")
print(f"intercept = {reg.intercept_}")
print(f"R^2 = {reg.score(X, Y)}")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 실제 값
ax.scatter(datasets['age'], datasets['experience'], datasets['income'], c='blue', marker='o', alpha=0.5)

# 예측한 값
test_X = np.array(
    list(
        map(lambda v: [v, randint(max(23, v - 20), v) - 20], [randint(23, 80) for _ in range(20)])
    )
)
print(f"test_X: {test_X}")

y_pred = reg.predict(test_X)
ax.scatter(datasets['age'], datasets['experience'], y_pred, c='yellow', marker='^', alpha=0.5)

# 모형 평면 그리기
xx, yy = np.meshgrid(datasets['age'].unique(), datasets['experience'].unique())
zz = reg.intercept_ + reg.coef_[0] * xx + reg.coef_[1] * yy

ax.plot_surface(xx, yy, zz, alpha=0.1)

ax.set_xlabel('Age')
ax.set_ylabel('Experience')
ax.set_zlabel('Income')

plt.show()