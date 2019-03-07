'''Tkinter教程之Font篇'''
# Tkinter中其它常用的一些功能
'''1.字体使用'''
# -*- coding: utf-8 -*-
# 改变组件的显示字体
from tkinter import *
import tkinter.font as tkFont

root = Tk()
font_list = tkFont.families()
# # 创建一个Label
font_list_final = []
for ft in font_list:
	tmp = ft.split(' ')
	if len(tmp)>1:
		continue
	font_list_final.append(ft)
for ft in font_list_final:
    Label(root, text=ft+' ;字体fds', font=ft).grid()
 
root.mainloop()
# 在Windows上测试字体显示，注意字体中包含有空格的字体名称必须指定为tuple类型。
