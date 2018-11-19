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

# === データ行列 ===
# 説明変数
dataset = xhamster_dataset[['nb_views', 'nb_comments', 'runtime']]
dataset = dataset.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
X = dataset[['nb_views', 'nb_comments', 'runtime']]
data_num = X.shape[0]
X = np.concatenate((np.ones([data_num, 1], dtype=np.float32), X), axis=1)
X = np.nan_to_num(X)

data_matrix = np.dot(X.T, X)

print(data_matrix)