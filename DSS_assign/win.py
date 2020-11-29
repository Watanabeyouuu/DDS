"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: win.py
@date: 2020/11/5 7:59 下午

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
import tkinter as tk
import tkinter.font as tf

from DSS_assign import ex1, km
from DSS_assign.write import write_ex1_1

data = []  # 存放三个系数
window = tk.Tk()
window.title('市场需求预测')
window.geometry('940x960')

frame0 = tk.Frame(window)
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)


# 定义触发事件时的函数
def insert_point():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')
    t3.delete(1.0, 'end')
    t4.delete(1.0, 'end')
    t5.delete(1.0, 'end')
    t6.delete(1.0, 'end')
    data = ex1.ex1_1()
    # print(data)
    t1.insert('insert', data[0])
    t2.insert('insert', data[1])
    t3.insert('insert', data[2])
    t4.insert('insert', data[3])
    t5.insert('insert', data[4])
    t6.insert('insert', data[5])


def show_result():
    res.delete(1.0, 'end')
    jiejv = t5.get('0.0', 'end')
    xishu = t6.get('0.0', 'end').replace('[', '').replace(']', '').split(' ')
    # print(xishu)
    X1 = float(e1.get())
    X2 = float(e2.get())
    X3 = float(e3.get())
    pre = float(jiejv) + float(xishu[0]) * X1 + float(xishu[2]) * X2 + float(xishu[4]) * X3
    res.insert('insert', pre)
    write_ex1_1.w_ex1_1(str(X1), str(X2), str(X3), str(pre))
    print('预测值：', pre)


ejbt = tf.Font(size=15)
ft = tf.Font(size=20)
tk.Label(frame0, text='决策支持系统', width=0, height=4, font=ft).grid(row=0, column=0)
# -------------ex1_1------------------------------------------------------
# 创建输入框entry
tk.Label(frame2, text='price', width=8).grid(row=0, column=0)
e1 = tk.Entry(frame2, width=8)
e1.grid(row=0, column=1)
tk.Label(frame2, text='expense', width=8).grid(row=1, column=0)
e2 = tk.Entry(frame2, width=8)
e2.grid(row=1, column=1)
tk.Label(frame2, text='production', width=8).grid(row=2, column=0)
e3 = tk.Entry(frame2, width=8)
e3.grid(row=2, column=1)

res = tk.Text(frame2, height=1, width=10)
res.grid(row=2, column=3)
b1 = tk.Button(frame2, text='预测结果', width=8, height=2, command=show_result)
b1.grid(row=4, column=1, sticky='w')
# 创建一个文本框用于显示
t1 = tk.Text(frame1, height=1, width=100)
t1.grid(row=1, column=1)
t2 = tk.Text(frame1, height=1, width=100)
t2.grid(row=2, column=1)
t3 = tk.Text(frame1, height=1, width=100)
t3.grid(row=3, column=1)
t4 = tk.Text(frame1, height=1, width=100)
t4.grid(row=4, column=1)
t5 = tk.Text(frame1, height=1, width=100)
t5.grid(row=5, column=1)
t6 = tk.Text(frame1, height=1, width=100)
t6.grid(row=6, column=1)

tk.Label(frame1, text='EX1_1 多元线性回归', width=20, height=3, font=ejbt).grid(row=0, column=0, padx=12)
tk.Label(frame1, text='公式', width=7).grid(row=1, column=0)
tk.Label(frame1, text='拟合效果', width=7).grid(row=2, column=0)
tk.Label(frame1, text='广告支出', width=7).grid(row=3, column=0)
tk.Label(frame1, text='价格下降', width=7).grid(row=4, column=0)
tk.Label(frame1, text='截距', width=7).grid(row=5, column=0)
tk.Label(frame1, text='系数', width=7).grid(row=6, column=0)
b1 = tk.Button(frame1, text='开始拟合', width=8, height=2, command=insert_point)
b1.grid(row=7, column=1, sticky='w')


# b1 = tk.Button(window, text='可视化', width=8, height=2, command=insert_point)
# b1.grid(row=4, column=5)

# photo = tk.PhotoImage(file='img/boxplot.png')  # file：t图片路径
# imgLabel = tk.Label(window, image=photo)  # 把图片整合到标签类中
# imgLabel.grid(row=5, column=0)  # 自动对齐
# -------------ex1_2------------------------------------------------------
def xxgh():
    xxgh_data = ex1.ex1_2()
    zdz.insert('insert', xxgh_data[0])
    hw.insert('insert', xxgh_data[1])
    zy.insert('insert', xxgh_data[2])
    qt.insert('insert', xxgh_data[3])


tk.Label(frame3, text='EX1_2 线性规划', width=17, height=3, font=ejbt).grid(row=0, column=0, padx=12)
tk.Label(frame3, text='最大值', width=7).grid(row=1, column=0)
tk.Label(frame3, text='户外广告', width=7).grid(row=2, column=0)
tk.Label(frame3, text='专业杂志', width=7).grid(row=3, column=0)
tk.Label(frame3, text='其他形式', width=7).grid(row=4, column=0)
# 创建一个文本框用于显示
zdz = tk.Text(frame3, height=1, width=60)
zdz.grid(row=1, column=1)
hw = tk.Text(frame3, height=1, width=60)
hw.grid(row=2, column=1, padx=1)
zy = tk.Text(frame3, height=1, width=60)
zy.grid(row=3, column=1)
qt = tk.Text(frame3, height=1, width=60)
qt.grid(row=4, column=1)
butt_gh = tk.Button(frame3, text='Max计算', width=8, height=2, command=xxgh)
butt_gh.grid(row=7, column=1, sticky='w')


# -------------ex2------------------------------------------------------
def km_cla():
    km1.delete(1.0, 'end')
    km2.delete(1.0, 'end')
    km3.delete(1.0, 'end')
    data = km.ex2()
    print(data)
    km1.insert('insert', data[0])
    km2.insert('insert', data[1])
    km3.insert('insert', data[2])


# 创建一个文本框用于显示
km1 = tk.Text(frame4, height=1, width=70)
km1.grid(row=1, column=1)
km2 = tk.Text(frame4, height=1, width=70)
km2.grid(row=2, column=1)
km3 = tk.Text(frame4, height=1, width=70)
km3.grid(row=3, column=1)

tk.Label(frame4, text='EX2 聚类 K-MEANS', width=17, height=3, font=ejbt).grid(row=0, column=0, padx=12)
tk.Label(frame4, text='第一类', width=7).grid(row=1, column=0)
tk.Label(frame4, text='第二类', width=7).grid(row=2, column=0)
tk.Label(frame4, text='第三类', width=7).grid(row=3, column=0)
km_b = tk.Button(frame4, text='开始聚类', width=6, height=2, command=km_cla)
km_b.grid(row=4, column=0)

frame0.grid(row=0, column=0)
frame1.grid(row=1, column=0)
frame2.grid(padx=60, pady=5, sticky='w')
frame3.grid(padx=1, pady=5, sticky='w')
frame4.grid(padx=1, pady=5, sticky='w')
window.mainloop()
