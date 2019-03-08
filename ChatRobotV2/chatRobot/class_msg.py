from tkinter import *
from tkinter import scrolledtext
import time
import random
import requests
import hashlib
import time
import json
from class_music import *
from class_data import *
from const_data import *
from class_conn_people import *

class Msg:

  def __init__(self,frame):
    # my message record
    self.int_msg = scrolledtext.ScrolledText(frame.fra_int,width=32,height=22,background="#c9daf8")
    self.int_msg.tag_configure('beg', foreground='#1c4587', 
                        font=font)
    self.int_msg.tag_configure('color', foreground='#3c78d8', 
                        font=font)
    # input box
    self.msg = scrolledtext.ScrolledText(frame.fra_msg,font=font,width=68,height=7,background="#e9e9e9")
    self.msg.tag_add('tag1', 1.0,8.0)
    self.msg.tag_configure('tag1',foreground='#1c4587',
                        font=font)
    self.auto_msg = scrolledtext.ScrolledText(frame.fra_auto,width=32,height=22,background="#dfd9ed") 
    self.auto_msg.tag_configure('automsg', foreground='#783f04', 
                        font=font)
    self.auto_msg.tag_configure('begin', foreground='#e69138', 
                        font=font)
    self.msg.tag_config('tag_msg',font=font)
    self.pos_reply = Data().get_data()

    self.bg_music = Music("./music/我的一个道姑朋友.mp3")
    self.send_music = Music()


  def create_conns(self):
    self.conns = [People(self,name) for name in conns_dict['people']]
    self.conns = self.conns + [Bolt(self,name) for name in conns_dict['bolt']]
    self.conns = self.conns + [Translator(self,name) for name in conns_dict['trans']]
    self.conns = self.conns + [MovieRecomm(self,name) for name in conns_dict['movie']]
    self.cur_conn = self.conns[0]


  # 发送按钮的快捷键设置
  def crt_but(self,frame):
    # 实现播放键能开始和从暂停中恢复两个功能
    # 背景音乐播放时，消息音效无  
    def sendmsg_event(e):
      if e.keysym=="Control_L":
        self.sendmsg()
    def start_bgmusic():
      Music.switch_on = False     
      self.bg_music.bg_sound()
    def pause_bgmusic(): 
      Music.switch_on = False     
      self.bg_music.track_pause()
    def stop_bgmusic(): 
      Music.switch_on = True     
      self.bg_music.track_stop()
    # 音乐按钮
    self.but_send = Button(frame.fra_but,font=font,text=u"发送",width=30,command=self.sendmsg)
    self.but_bgMusic = Button(frame.fra_sen,font=font,text=u"音乐开始",width=30,command=start_bgmusic)
    self.but_bgMusic_pause = Button(frame.fra_sen,font=font,text=u"音乐暂停",width=30,command=pause_bgmusic)
    self.but_bgMusic_stop = Button(frame.fra_sen,font=font,text=u"音乐结束",width=30,command=stop_bgmusic)
    self.msg.bind('<Control_L>',sendmsg_event)
    # 联系人按钮
    for conn in self.conns:
      conn.create_button(frame)


  def crt_grid(self):
    self.but_send.pack(side="left")
    self.int_msg.grid()
    self.msg.grid()
    self.auto_msg.grid()
    self.but_bgMusic.pack(side="left")
    self.but_bgMusic_pause.pack(side="left")
    self.but_bgMusic_stop.pack(side="left")

    for conn in self.conns:
      if conn == self.conns[0]:
        conn.button.pack(side='top')
      else:
        conn.button.pack()

  # 自动回复，设随机数，规定回复的格式细节
  def auto_reply(self):
    fin_msg = self.cur_conn.auto_reply()
    self.auto_msg.insert(END, self.cur_conn.reply_name+": ", 'begin')
    self.auto_msg.insert(END, fin_msg, 'automsg')

  # 按下发送按钮之后的操作，实现消息上传以及智能回复
  def sendmsg(self):
    if Music.switch_on:
      self.send_music.msg_sound()

    intro = "少爷: "
    raw_sen = self.msg.get('0.0',END)
    self.cur_conn.change_msg_for_url(raw_sen)
    # 实现自学习，得到用户的语句，之后进行分析，做出回答
    # with open("D:\\text\\result.txt",'a') as f:
    #     f.write(raw_sen)
    self.int_msg.insert(END, intro,'color')
    self.int_msg.insert(END, self.msg.get('0.0',END)+'\n','beg')
    # print(self.int_msg.get('1.0','end-1c'))
    self.msg.delete('0.0',END)
    self.auto_reply()
    self.int_msg.see(END)
    self.msg.see(END)
    self.auto_msg.see(END)
    
