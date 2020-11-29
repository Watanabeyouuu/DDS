"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: km.py
@date: 2020/11/5 6:11 下午

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳ ┃
            ┃     ┻   ┃
            ┗━┓     ┏━┛
              ┃     ┗━━━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗━━━┓┓┏━━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from DSS_assign.read import read_ex2
from collections import Counter


def ex2():
    print("connecting database...")
    df = read_ex2.rdata_ex2()
    # df = pd.read_csv('data/ex2.csv', header=0, encoding='utf-8')
    # print(df)
    df1 = df.iloc[:, 1:]
    # print(df1)
    c_num = 5
    kmeans = KMeans(n_clusters=c_num, random_state=10).fit(df1)
    df1['jllable'] = kmeans.labels_
    df_count_type = df1.groupby('jllable').apply(np.size)

    # 各个类别的数目
    # print(df_count_type)
    # 聚类中心
    print(kmeans.cluster_centers_)
    # 新的dataframe，命名为new_df ，并输出到本地，命名为new_df.csv。
    new_df = df1[:]
    k_lst = list(new_df['jllable'])
    # print(k_lst)
    counter = Counter(k_lst)
    print(counter.values())

    new_df.to_csv('new_df.csv')

    # 将用于聚类的数据的特征的维度降至2维，并输出降维后的数据，形成一个dataframe名字new_pca
    pca = PCA(n_components=2)
    new_pca = pd.DataFrame(pca.fit_transform(new_df))
    print(new_df)
    print(new_pca)

    # 可视化
    # for i in range(0, c_num):
    d = new_pca[new_df['jllable'] == 0]
    plt.plot(d[0], d[1], 'r.')
    print('d[0]', d[0], '======')
    d = new_pca[new_df['jllable'] == 1]
    plt.plot(d[0], d[1], 'go')
    d = new_pca[new_df['jllable'] == 2]
    plt.plot(d[0], d[1], 'b*')
    d = new_pca[new_df['jllable'] == 3]
    plt.plot(d[0], d[1], 'g*')
    plt.gcf().savefig('img/kmeans.png')
    plt.show()

    waters = ('0', '1', '2')
    buy_number = [counter[0], counter[1], counter[2]]
    plt.barh(waters, buy_number)  # 横放条形图函数 barh
    plt.title('Customer Type')
    plt.savefig('img/kmeans_tx.png')
    plt.show()
    return counter[0], counter[1], counter[2]


if __name__ == '__main__':
    ex2()
