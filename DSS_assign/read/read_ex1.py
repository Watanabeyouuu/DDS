"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: read_ex1.py
@date: 2020/11/6 1:45 下午

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
import pandas as pd
import numpy as np
import pymysql


# 链接数据库，分别是IP，端口，用户名，密码，数据库，编码形式，注意这里的密码和IP我隐藏了，请自己输入你的
def rdata_ex1():
    con = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='DSS', charset='utf8')
    cursor = con.cursor()
    sql = 'SELECT * FROM ex1'
    cursor.execute(sql)
    data = cursor.fetchall()
    # print("转化前\n",data)
    # 直接转化出现错误
    data_ex1_df = pd.DataFrame(data)
    # print(data_ex1_df)
    # print("转化后\n",data_df)
    return data_ex1_df