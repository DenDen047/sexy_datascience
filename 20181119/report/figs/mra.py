import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

DATASET_DIR = '/data'

# === データセットの読み込み ===
path = os.path.join(DATASET_DIR, 'xhamster.csv')
xhamster_dataset = pd.read_csv(path, sep=",")
xhamster_dataset.info()
xhamster_dataset.head()  # データを表示

# === 重回帰分析 ===
from sklearn import linear_model
clf = linear_model.LinearRegression()

# データの標準化
dataset = xhamster_dataset[['nb_views', 'nb_comments', 'runtime', 'nb_votes']]
dataset = dataset.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
print(dataset.head())
print('')

# 説明変数
xs = dataset[['nb_views', 'nb_comments', 'runtime']]
X = xs.values
# 目的変数
Y = dataset['nb_votes'].values

X = np.nan_to_num(X)
Y = np.nan_to_num(Y)
print('X shape: {}'.format(X.shape))
print('Y shape: {}'.format(Y.shape))
print('')

# 予測モデルを作成
clf.fit(X, Y)

# 偏回帰係数
print(pd.DataFrame({
    "Name": xs.columns,
    "Coefficients": clf.coef_
}).sort_values(by='Coefficients') )

# 切片 (誤差)
print(clf.intercept_)