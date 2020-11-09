"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: km_win.py
@date: 2020/11/6 1:16 下午

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

from PIL import ImageTk

from DSS_assign import km

window = tk.Tk()
window.title('客户聚类')
window.geometry('350x180')

# 创建输入框entry，用户输入任何内容都显示为*

# 创建一个文本框用于显示
t1 = tk.Text(window, height=1, width=70)
t1.grid(row=0, column=1)
t2 = tk.Text(window, height=1, width=70)
t2.grid(row=1, column=1)
t3 = tk.Text(window, height=1, width=70)
t3.grid(row=2, column=1)
t4 = tk.Text(window, height=1, width=70)
t4.grid(row=3, column=1)


# 定义触发事件时的函数
def insert_point():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')
    t3.delete(1.0, 'end')

    data = km.ex2()
    print(data)
    t1.insert('insert', data[0])
    t2.insert('insert', data[1])
    t3.insert('insert', data[2])


# def showImg():
    # load = tk.Image.open('img/kmeans.png')
    # render = ImageTk.PhotoImage(load)
    # img = tk.Label(image=render)
    # img.image = render
    # img.place(x=0, y=0)
    # photo = tk.PhotoImage(file='img/kmeans.png')  # file：t图片路径
    # imgLabel = tk.Label(window, image=photo)  # 把图片整合到标签类中
    # imgLabel.grid(row=5, column=0)  # 自动对齐


tk.Label(text='第一类', width=7).grid(row=0, column=0)
tk.Label(text='第二类', width=7).grid(row=1, column=0)
tk.Label(text='第三类', width=7).grid(row=2, column=0)
b1 = tk.Button(window, text='开始拟合', width=6, height=2, command=insert_point)
b1.grid(row=4, column=1)
# b1 = tk.Button(window, text='可视化', width=8, height=2, command=showImg)
# b1.grid(row=4, column=0)
# b1 = tk.Button(window, text='可视化', width=8, height=2, command=insert_point)
# b1.grid(row=4, column=5)

# photo = tk.PhotoImage(file='img/kmeans.png')  # file：t图片路径
# imgLabel = tk.Label(window, image=photo)  # 把图片整合到标签类中
# imgLabel.grid(row=5, column=1)  # 自动对齐


window.mainloop()
