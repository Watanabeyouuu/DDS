"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: ex1_lr.py
@date: 2020/11/5 3:43 下午

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
from builtins import print

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import optimize as op
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def ex1_1():
    # sales = read_ex1.rdata_ex1()
    # sales.columns = ['year', 'sales', 'price', 'expenses', 'production']
    sales = pd.read_csv("data/ex1.csv")
    sales = pd.DataFrame(sales)
    print(sales)
    # print(sales.iloc[:, 1:5])
    s_data = sales.iloc[:, 1:5]
    # print(s_data)
    # print(sales.iloc[:, 2:])
    # 数据描述
    # print(s_data.describe())
    s_data.boxplot()
    plt.savefig('img/boxplot.png')
    plt.show()
    sns.pairplot(s_data, x_vars=["sales", "price", "expenses", "production"], y_vars='sales', height=7, aspect=0.8)
    # 相关系数0~0.3弱相关0.3~0.6中等程度相关0.6~1强相关
    # print(s_data.corr())
    sns.pairplot(s_data, x_vars=["sales", "price", "expenses", "production"], y_vars='sales', height=7, kind='reg')
    plt.savefig("img/pair.jpg")
    plt.show()

    X_train, X_test, Y_train, Y_test = train_test_split(sales.iloc[:, 2:], sales.sales, train_size=.70, random_state=0)
    print("原始数据特征:", sales.iloc[:, 2:].shape,
          ",训练数据特征:", X_train.shape,
          ",测试数据特征:", X_test.shape)

    print("原始数据标签:", sales.sales.shape,
          ",训练数据标签:", Y_train.shape,
          ",测试数据标签:", Y_test.shape)

    model = LinearRegression()
    model.fit(X_train, Y_train)
    a = model.intercept_  # 截距
    b = model.coef_  # 回归系数
    print("最佳拟合线:截距", a, ",回归系数：", b)

    score = model.score(X_test, Y_test)
    print("拟合效果", score)
    # 对线性回归进行预测
    Y_pred = model.predict(X_test)
    # print("X_test", X_test)
    # print(Y_pred)
    plt.plot(range(len(Y_pred)), Y_pred, 'b', label="predict")
    # 显示图像
    plt.savefig("img/predict.jpg")
    plt.show()
    plt.figure()
    plt.plot(range(len(Y_pred)), Y_pred, 'b', label="predict")
    plt.plot(range(len(Y_pred)), Y_test, 'r', label="test")
    plt.legend(loc="upper right")  # 显示图中的标签
    plt.xlabel("the number of sales")
    plt.ylabel('value of sales')
    plt.savefig("img/ROC.jpg")
    plt.show()

    # def predict(price, exp, pro):
    #     sales = a + b[0] * price + b[1] * exp + b[2] * pro
    #     return sales
    pre_expense = (265.32130 * 1.1 - b[0] * 41.26383 - b[2] * 157.00 - a) / b[1]
    print('广告支出费需要达到:', pre_expense)
    pre_price = (265.32130 * 1.1 - b[1] * 114.18541 - b[2] * 157.00 - a) / b[0]
    print('价格下降到到:', pre_price)
    return "y = %s + %sxX1 + %sxX2 + %sxX3" % (a, b[0], b[1], b[2]), score, pre_expense, pre_price, a, b


def ex1_2():
    c = np.array([192, 36, 12])
    A_ub = np.array([[150000, 24000, 120000], [-150000, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 0, -3]])
    B_ub = np.array([1000000, -650000, -2, -3, 2])
    # A_eq = np.array([[1, 1, 1]])
    # B_eq = np.array([7])
    x1 = (0, 999)
    x2 = (0, 999)
    x3 = (0, 999)
    res = op.linprog(-c, A_ub, B_ub, bounds=(x1, x2, x3))
    print(res)
    print("---------------------------------------------")
    print("最大值为:", int(-res.fun))
    print("户外广告：", round(res.x[0]), "专业杂志：", round(res.x[1]), "其他形式：", round(res.x[2]))
    return int(-res.fun), round(res.x[0]), round(res.x[1]), round(res.x[2])


if __name__ == '__main__':
    ex1_1()
    ex1_2()
