"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: write_ex1_1.py
@date: 2020/11/9 1:17 下午

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
import csv
import re

import pymysql


def w_ex1_1(e1, e2, e3, pre):
    try:
        db = pymysql.connect("localhost", "root", "123456", "DSS", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        insert_sql = "INSERT INTO " + "predict_sales" + \
                     " (`price`, `expenses`, `production`, `pre_sales`) " \
                     "values (%s, %s, %s, %s)"
        val = (e1, e2, e3, pre)
        cursor.execute(insert_sql, val)
        db.commit()
    except Exception as e:
        print(e)
        # Rollback in case there is any error
        db.rollback()

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    w_ex1_1('12', '2', '4', '6')