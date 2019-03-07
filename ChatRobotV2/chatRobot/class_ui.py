from tkinter import *

class UI:

  def __init__(self):
   self.fra_cnt = Frame(width=150,height=409,bg="gray")
   self.fra_int = Frame(width=250,height=300,bg="white")
   self.fra_auto = Frame(width=250,height=300,bg="white")
   self.fra_msg = Frame(width=500,height=100,bg="white")
   self.fra_img = Frame(width=100,height=409,bg="white")
   self.fra_sen = Frame(width=655,height=20,bg="#00ff88")
   self.fra_but = Frame(width=100,height=20,bg="gray")
    # 创建几个区域划分，指定每块的大小，颜色等属性
    # 以后：加进头像，音乐，动画

  # 规划以及显示总体布局
  def crt_grid(self):

    self.fra_cnt.grid(row=0,rowspan=5,column=0,padx=6,pady=6)
    self.fra_int.grid(row=0,rowspan=4,column=1,pady=6)
    self.fra_auto.grid(row=0,rowspan=4,column=2,pady=6)
    self.fra_msg.grid(row=4,column=1,columnspan=2,padx=3)
    self.fra_img.grid(row=0,rowspan=5,column=3,padx=3)
    self.fra_sen.grid(row=5,column=0,columnspan=3,padx=2,pady=6)
    self.fra_but.grid(row=5,column=3)

    # replace below calls
    for k, v in vars(self).items():
      eval('self.'+k).grid_propagate(0)
      
    # self.fra_cnt.grid_propagate(0)
    # self.fra_int.grid_propagate(0)
    # self.fra_auto.grid_propagate(0)
    # self.fra_msg.grid_propagate(0)
    # self.fra_img.grid_propagate(0)
    # self.fra_sen.grid_propagate(0)
    # self.fra_but.grid_propagate(0)