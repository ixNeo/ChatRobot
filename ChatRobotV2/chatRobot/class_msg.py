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

    self.kind = ""
    self.msg_for_url = ""
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

    self.conns = [Connector(name) for name in name_list]
    self.i = random.randint(0, len(self.pos_reply))
    self.j = 0

    self.reply_name = u"皮皮熊"
  # sc_msg = Scrollbar(fra_msg)


  # 自动回复，设随机数，规定回复的格式细节
  def auto_reply(self):
    if self.kind == 'bolt':
      key = "86a516ab67a64ed29f28bb683e77e1f8"      
      url = "http://www.tuling123.com/openapi/api?key=" + key + "&info=" + self.msg_for_url
      html = requests.get(url)
      fin_msg = html.json()['text']+'\n'
    elif self.kind == '汉译英':
      appKey = '397d5478d0f3fa46'
      secretKey = 'H3c6MnnBgL4Itq0uR5ajz6Muca4XxJIO'
      q = self.msg_for_url
      salt = str(time.time())[:10]
      sign = appKey+q+salt+secretKey
      sign = hashlib.md5(sign.encode("utf-8")).hexdigest()
      url = "http://openapi.youdao.com/api"
      params = {
                  'q':q.encode('utf-8'),
                  'from':'zh',
                  'to':'en',
                  'appKey':appKey,
                  'salt': salt,
                  'sign':sign
                  }
      html = requests.get(url,params=params)
      html.encoding = html.apparent_encoding
      html = html.text
      res = json.loads(html)
      fin_msg = res['translation'][0]+'\n'
    elif self.kind == '英译汉':
      appKey = '397d5478d0f3fa46'
      secretKey = 'H3c6MnnBgL4Itq0uR5ajz6Muca4XxJIO'
      q = self.msg_for_url
      salt = str(time.time())[:10]
      sign = appKey+q+salt+secretKey
      sign = hashlib.md5(sign.encode("utf-8")).hexdigest()
      url = "http://openapi.youdao.com/api"
      params = {
                  'q':q.encode('utf-8'),
                  'from':'en',
                  'to':'zh',
                  'appKey':appKey,
                  'salt': salt,
                  'sign':sign
                  }
      html = requests.get(url,params=params)
      html.encoding = html.apparent_encoding
      html = html.text
      res = json.loads(html)
      fin_msg = res['translation'][0]+'\n'
    else:
      while self.i==self.j:
        self.i = random.randint(0, len(self.pos_reply))
      self.j = self.i
      fin_msg = self.pos_reply[self.i]+'\n'
    self.auto_msg.insert(END, self.reply_name+": ", 'begin')
    self.auto_msg.insert(END, fin_msg, 'automsg')


  # 按下发送按钮之后的操作，实现消息上传以及智能回复
  def sendmsg(self):

    if Music.switch_on:
      self.send_music.msg_sound()

    intro = u">:"
    raw_sen = self.msg.get('0.0',END)
    self.msg_for_url = raw_sen
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
    self.but_send = Button(frame.fra_but,font=font,text=u"音乐开始",width=30,command=self.sendmsg)
    self.but_bgMusic = Button(frame.fra_sen,font=font,text=u"音乐开始",width=30,command=start_bgmusic)
    self.but_bgMusic_pause = Button(frame.fra_sen,font=font,text=u"音乐暂停",width=30,command=pause_bgmusic)
    self.but_bgMusic_stop = Button(frame.fra_sen,font=font,text=u"音乐结束",width=30,command=stop_bgmusic)
    self.msg.bind('<Control_L>',sendmsg_event)

    # 联系人按钮
    def create_people_btn(self,name):
      print('ch-name',name[0])
      chinese_name = name[0]
      index_name = name[1]
      def cnt_people(self):
        cntor = Data(name_file_dict[index_name])
        self.pos_reply = cntor.get_data()
        self.i = random.randint(0, len(self.pos_reply))
        self.j = 0
        self.reply_name=chinese_name
        self.kind = 'people'
      def cnt_movie(self):
        cntor = Data("./text/db_movie.txt")
        self.pos_reply = cntor.get_data()
        self.i = random.randint(0, len(self.pos_reply))
        self.j = 0
        self.reply_name=u"电影推荐"
        self.kind = 'movie'
      def cnt_trans(self):
        self.kind = chinese_name
        self.reply_name=chinese_name
      # print('clicked connect people button.......')
      if index_name in name_file_dict.keys(): 
        print('people')
        return cnt_people
      elif chinese_name==u"电影推荐":
        print('movie') 
        return cnt_movie
      else: 
        print('alice/trans')
        return cnt_trans

    people_btn_dict = {}
    for name in name_list:
      print('start',name)
      people_btn_dict[name[1]] = create_people_btn(self,name)
      print('end',name)


    # def cnt1(self):
    #   cntor = Data("./text/xiongchuyuan.txt")
    #   self.pos_reply = cntor.get_data()
    #   self.i = random.randint(0, len(self.pos_reply))
    #   self.j = 0
    #   self.reply_name=u"皮皮熊"
    #   self.kind = 'person'

    # def cnt2(self):
    #   cntor = Data("./text/jingda_duzou.txt")
    #   self.pos_reply = cntor.get_data()
    #   self.i = random.randint(0, len(self.pos_reply))
    #   self.j = 0
    #   self.reply_name=u"社会阿达"
    #   self.kind = 'person'

    # def cnt3(self):
    #   cntor = Data("./text/xiaochen_duzou.txt")
    #   self.pos_reply = cntor.get_data()
    #   self.i = random.randint(0, len(self.pos_reply))
    #   self.j = 0
    #   self.reply_name=u"大姐大"
    #   self.kind = 'person'

    # def cnt4(self):
    #   cntor = Data("./text/yutian_duzou.txt")
    #   self.pos_reply = cntor.get_data()
    #   self.i = random.randint(0, len(self.pos_reply))
    #   self.j = 0
    #   self.reply_name=u"小蠢货"
    #   self.kind = 'person'

    # def cnt5(self):
    #   cntor = Data("./text/haodong_duzou.txt")
    #   self.pos_reply = cntor.get_data()
    #   self.i = random.randint(0, len(self.pos_reply))
    #   self.j = 0
    #   self.reply_name=u"秃顶大叔"
    #   self.kind = 'person'

    # def cnt6(self):
    #   cntor = Data("./text/poem.txt")
    #   self.pos_reply = cntor.get_data()
    #   self.i = random.randint(0, len(self.pos_reply))
    #   self.j = 0
    #   self.reply_name=u"明楼"
    #   self.kind = 'person'

    # def cnt7(self):
    #   cntor = Data("./text/result.txt")
    #   self.pos_reply = cntor.get_data()
    #   self.i = random.randint(0, len(self.pos_reply))
    #   self.j = 0
    #   self.reply_name=u"心灵捕手"
    #   self.kind = 'person'

    # def cnt8(self):
    #   self.kind = "bolt"
    #   self.reply_name="Alice"

    # def cnt9(self):
    #   self.kind = "汉译英"
    #   self.reply_name="translater"

    # def cnt10(self):
    #   self.kind = "英译汉"
    #   self.reply_name="translater"

    # def cnt11(self):
    #   cntor = Data("./text/db_movie.txt")
    #   self.pos_reply = cntor.get_data()
    #   self.i = random.randint(0, len(self.pos_reply))
    #   self.j = 0
    #   self.reply_name=u"电影推荐"
    #   self.kind = 'movie'

    # image=ImageTk.PhotoImage(Image.open("D:\\python_play\\chatbolt\\image\\cool.jpg"))

    # print(globals()['Msg'])
    # print(eval('self'))

    funcname = people_btn_dict['da']
    # funcname()
        # print('*'*50) eval('self.but_'+name[1])
    setattr(self,'but_da',Button(frame.fra_cnt,text='da',font=font,fg=fg_color,bg=bg_color,width=width,command=lambda:funcname(self)))
    funcname = people_btn_dict['sister']
    setattr(self,'but_sister',Button(frame.fra_cnt,text='da',font=font,fg=fg_color,bg=bg_color,width=width,command=lambda:funcname(self)))
    for name in name_list:
      if name not in [(u"社会阿达",'da'),(u"大姐大",'sister')]:
        setattr(self,'but_'+name[1],Button(frame.fra_cnt,text=name[0],font=font,fg=fg_color,bg=bg_color,width=width))




    # for name in name_list:
    #   funcname = people_btn_dict[name[1]]
    #   funcname()
    #     # print('*'*50) eval('self.but_'+name[1])
    #   setattr(self,'but_'+name[1],Button(frame.fra_cnt,text=name[0],font=font,fg=fg_color,bg=bg_color,width=width,command=lambda:funcname(self)))




      # print(eval('self.but_'+name[1]))
        # print(globals()['Msg'],'but_cnt'+name[1])
        # print(locals()['self'].__attr__)
        # print(locals()['self.but_'+name[1]])
        # print(eval('self.but_'+name[1]))
    # self.but_cnt1 = Button(frame.fra_cnt,text=u"皮皮熊",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt1(self))
    # self.but_cnt2 = Button(frame.fra_cnt,text=u"社会阿达",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt2(self))
    # self.but_cnt3 = Button(frame.fra_cnt,text=u"大姐大",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt3(self))
    # self.but_cnt4 = Button(frame.fra_cnt,text=u"小蠢货",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt4(self))
    # self.but_cnt5 = Button(frame.fra_cnt,text=u"秃顶大叔",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt5(self))
    # self.but_cnt6 = Button(frame.fra_cnt,text=u"明楼",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt6(self))
    # self.but_cnt7 = Button(frame.fra_cnt,text=u"心灵捕手",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt7(self))
    # self.but_cnt8 = Button(frame.fra_cnt,text=u"Alice",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt8(self))
    # self.but_cnt9 = Button(frame.fra_cnt,text=u"汉译英",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt9(self))
    # self.but_cnt10 = Button(frame.fra_cnt,text=u"英译汉",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt10(self))
    # self.but_cnt11 = Button(frame.fra_cnt,text=u"电影推荐",font=('幼圆',12,'bold'),fg='#6600cc',bg='#ccffcc',width=20,command=lambda:cnt11(self))

  def crt_grid(self):

    self.but_send.pack(side="left")
    self.int_msg.grid()
    self.msg.grid()
    self.auto_msg.grid()
    self.but_bgMusic.pack(side="left")
    self.but_bgMusic_pause.pack(side="left")
    self.but_bgMusic_stop.pack(side="left")

    for name in name_list:
      if name==name_list[0]:
        eval('self.but_'+name[1]).pack(side='top')
      else:
        eval('self.but_'+name[1]).pack()
    # self.but_cnt1.pack(side="top")
    # self.but_cnt2.pack()
    # self.but_cnt3.pack()
    # self.but_cnt4.pack()
    # self.but_cnt5.pack()
    # self.but_cnt6.pack()
    # self.but_cnt7.pack()
    # self.but_cnt8.pack()
    # self.but_cnt9.pack()
    # self.but_cnt10.pack()
    # self.but_cnt11.pack()