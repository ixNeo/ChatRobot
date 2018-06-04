from tkinter import *
from tkinter import scrolledtext
import time
import random

from class_music import *
from class_data import *

class Msg:

  def __init__(self,frame):

    self.int_msg = scrolledtext.ScrolledText(frame.fra_int,width=32,height=22)
    self.msg = scrolledtext.ScrolledText(frame.fra_msg,width=68,height=7)
    self.auto_msg = scrolledtext.ScrolledText(frame.fra_auto,width=32,height=22) 
    self.msg.tag_config('tag_msg',font="宋体")
    self.pos_reply = Data().get_data()

    self.bg_music = Music("./music/我的一个道姑朋友.mp3")
    self.send_music = Music()

    self.i = random.randint(0, len(self.pos_reply))
    self.j = 0

    self.reply_name = "皮皮熊"
  # sc_msg = Scrollbar(fra_msg)


  # 自动回复，设随机数，规定回复的格式细节
  def auto_reply(self):

    while self.i==self.j:
      self.i = random.randint(0, len(self.pos_reply))
    self.j = self.i
    fin_msg = self.reply_name+": "+ self.pos_reply[self.i]+'\n'
    self.auto_msg.insert(END, fin_msg)


  # 按下发送按钮之后的操作，实现消息上传以及智能回复
  def sendmsg(self):

    if Music.switch_on:
      self.send_music.msg_sound()

    intro = u"少爷:"
    raw_sen = self.msg.get('0.0',END)
    # 实现自学习，得到用户的语句，之后进行分析，做出回答
    # with open("D:\\text\\result.txt",'a') as f:
    #     f.write(raw_sen)
    self.int_msg.insert(END, intro)
    self.int_msg.insert(END, self.msg.get('0.0',END)+'\n')
    self.msg.delete('0.0',END)
    self.auto_reply()
    self.int_msg.see(END)
    self.msg.see(END)
    self.auto_msg.see(END)
    


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
    self.but_send = Button(frame.fra_but,text=u"发送",width=30,command=self.sendmsg)
    self.but_bgMusic = Button(frame.fra_sen,text=u"音乐开始",width=30,command=start_bgmusic)
    self.but_bgMusic_pause = Button(frame.fra_sen,text=u"音乐暂停",width=30,command=pause_bgmusic)
    self.but_bgMusic_stop = Button(frame.fra_sen,text=u"音乐结束",width=30,command=stop_bgmusic)
    self.msg.bind('<Control_L>',sendmsg_event)

    # 联系人按钮
    def cnt1(self):
      cntor = Data("./text/xiongchuyuan.txt")
      self.pos_reply = cntor.get_data()
      self.i = random.randint(0, len(self.pos_reply))
      self.j = 0
      self.reply_name=u"皮皮熊"

    def cnt2(self):
      cntor = Data("./text/jingda_duzou.txt")
      self.pos_reply = cntor.get_data()
      self.i = random.randint(0, len(self.pos_reply))
      self.j = 0
      self.reply_name=u"社会阿达"

    def cnt3(self):
      cntor = Data("./text/xiaochen_duzou.txt")
      self.pos_reply = cntor.get_data()
      self.i = random.randint(0, len(self.pos_reply))
      self.j = 0
      self.reply_name=u"大姐大"

    def cnt4(self):
      cntor = Data("./text/yutian_duzou.txt")
      self.pos_reply = cntor.get_data()
      self.i = random.randint(0, len(self.pos_reply))
      self.j = 0
      self.reply_name=u"小蠢货"

    def cnt5(self):
      cntor = Data("./text/haodong_duzou.txt")
      self.pos_reply = cntor.get_data()
      self.i = random.randint(0, len(self.pos_reply))
      self.j = 0
      self.reply_name=u"秃顶大叔"

    def cnt6(self):
      cntor = Data("./text/poem.txt")
      self.pos_reply = cntor.get_data()
      self.i = random.randint(0, len(self.pos_reply))
      self.j = 0
      self.reply_name=u"明楼"

    def cnt7(self):
      cntor = Data("./text/result.txt")
      self.pos_reply = cntor.get_data()
      self.i = random.randint(0, len(self.pos_reply))
      self.j = 0
      self.reply_name==u"心灵捕手"

    # image=ImageTk.PhotoImage(Image.open("D:\\python_play\\chatbolt\\image\\cool.jpg"))
    self.but_cnt1 = Button(frame.fra_cnt,text=u"皮皮熊",width=20,command=lambda:cnt1(self))
    self.but_cnt2 = Button(frame.fra_cnt,text=u"社会阿达",width=20,command=lambda:cnt2(self))
    self.but_cnt3 = Button(frame.fra_cnt,text=u"大姐大",width=20,command=lambda:cnt3(self))
    self.but_cnt4 = Button(frame.fra_cnt,text=u"小蠢货",width=20,command=lambda:cnt4(self))
    self.but_cnt5 = Button(frame.fra_cnt,text=u"秃顶大叔",width=20,command=lambda:cnt5(self))
    self.but_cnt6 = Button(frame.fra_cnt,text=u"明楼",width=20,command=lambda:cnt6(self))
    self.but_cnt7 = Button(frame.fra_cnt,text=u"心灵捕手",width=20,command=lambda:cnt7(self))


  def crt_grid(self):

    self.but_send.pack(side="left")
    self.int_msg.grid()
    self.msg.grid()
    self.auto_msg.grid()
    self.but_bgMusic.pack(side="left")
    self.but_bgMusic_pause.pack(side="left")
    self.but_bgMusic_stop.pack(side="left")

    self.but_cnt1.pack(side="top")
    self.but_cnt2.pack()
    self.but_cnt3.pack()
    self.but_cnt4.pack()
    self.but_cnt5.pack()
    self.but_cnt6.pack()
    self.but_cnt7.pack()