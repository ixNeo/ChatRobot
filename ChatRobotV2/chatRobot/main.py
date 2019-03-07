from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk
# from PIL import Image
import PIL.Image
import pygame
import time
import random


from class_msg import *
from class_ui import *
from class_music import *
from class_data import *

def main():

  # 两个主要类：UI和Msg ; 两个工具类：Data和Music
  root = Tk()
  root.title("chatterbot")
  # root.iconbitmap('image/cat32.ico')

  ui_win = UI()
  ui_win.crt_grid()

  msg_win = Msg(ui_win)
  msg_win.crt_but(ui_win)
  msg_win.crt_grid()

  # 图片变量的作用域必须与mainloop相同，因为没有设置全局变量，所以一并写在主函数中
  pic = PIL.Image.open("image/foxgirl.jpg")
  m1 = ImageTk.PhotoImage(pic)
  label1 = Label(ui_win.fra_img,compound="top",image=m1)
  label1.pack()

  root.mainloop()
  
 

if __name__=="__main__":
  main()

