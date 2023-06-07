from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from pandasql import sqldf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

lung_cap = pd.read_csv("LungCapData2.csv")

X = sqldf("""
    select Age, Height,
        case when Smoke = 'yes' then 1
            else 0
            end as Smoke,
        case when Gender = 'female' then 0
            else 1
            end as Gender
    from lung_cap
""")
Y = sqldf("""
    select LungCap
    from lung_cap
""")

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# MEAN SQUARE ERROR, 평균 제곱 오차
reg = SVR(C=10, epsilon=0.2, kernel="precomputed")
reg.fit(x_train, np.ravel(y_train))

y_pred = reg.predict(x_test)
mse = mean_squared_error(y_test, y_pred)

print(f"MSE: {mse}")

# 데이터의 차원을 2D로 축소
pca = PCA(n_components=2)
x_train_2d = pca.fit_transform(x_train)
x_test_2d = pca.fit_transform(x_test)

# 데이터를 하나의 DataFrame에 합칩니다.
data = np.hstack([x_train, y_train])
columns = ['Age', 'Height', 'Smoke', 'Gender', 'Lung Capacity']
df_train = pd.DataFrame(data, columns=columns)

# 서브그래프를 나타내기 위해 1x2 형태의 그리드
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# 상관 관계 행렬 계산 및 히트맵 생성
corr_matrix = df_train.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=1, vmin=-1, cbar_kws={'shrink': .8}, ax=ax1)
ax1.set_title('Heatmap of Correlation')

# 3D 그래프 생성
ax_3d = fig.add_subplot(122, projection='3d')
ax_3d.scatter(x_train_2d[:, 0], x_train_2d[:, 1], y_train, c='blue', marker='o', alpha=0.5)  # 파란색 -> 훈련 데이터셋
ax_3d.scatter(x_test_2d[:, 0], x_test_2d[:, 1], y_test, c='red', marker='*', alpha=0.5)  # 빨간색 -> 테스트 데이터셋
ax_3d.scatter(x_test_2d[:, 0], x_test_2d[:, 1], y_pred, c='yellow', marker='^', alpha=0.5)  # 노란색 -> 예측 결과
ax_3d.set_zlabel('Lung Capacity')
ax_3d.set_title('Test Data vs Predicted Data Comparison')

# 그래프를 보여줌
plt.show()