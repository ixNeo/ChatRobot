from tkinter import *
from tkinter import scrolledtext
import time
import random
import requests
import hashlib
import time
import json
from class_data import *
from const_data import *


class Connector:
	def __init__(self,msg,name):
		self.reply_name = name[0]
		self.index_name = name[1]
		self.msg_for_url = ""
		# self.msg represents object Msg
		self.msg = msg

	def create_button(self,frame):
		def btn_func(self):
			self.msg.cur_conn = self
		self.button = Button(frame.fra_cnt,text=self.reply_name,font=font,fg=fg_color,bg=bg_color,width=width,command=lambda:btn_func(self))

	def change_msg_for_url(self,msg_for_url):
		self.msg_for_url = msg_for_url



class Bolt(Connector):
	def __init__(self,msg,name):
		Connector.__init__(self,msg,name)
		  # 自动回复，设随机数，规定回复的格式细节
	def auto_reply(self):
		key = "86a516ab67a64ed29f28bb683e77e1f8"      
		url = "http://www.tuling123.com/openapi/api?key=" + key + "&info=" + self.msg_for_url
		html = requests.get(url)
		fin_msg = html.json()['text']+'\n'
		return fin_msg



class Translator(Connector):
	def __init__(self,msg,name):
		Connector.__init__(self,msg,name)
		self.appKey = eval(name[1]+'_appKey')
		self.secretKey = eval(name[1]+'_secretKey')
		self.url = "http://openapi.youdao.com/api"

	def auto_reply(self):
		q = self.msg_for_url
		salt = str(time.time())[:10]
		sign = self.appKey+q+salt+self.secretKey
		sign = hashlib.md5(sign.encode("utf-8")).hexdigest()
		params = {
				'q':q.encode('utf-8'),
				'from':self.index_name[:2],
				'to':self.index_name[3:],
				'appKey':self.appKey,
				'salt': salt,
				'sign':sign
				}
		html = requests.get(self.url,params=params)
		html.encoding = html.apparent_encoding
		html = html.text
		# print(html)
		res = json.loads(html)
		# print(res)
		fin_msg = res['translation'][0]+'\n'
		return fin_msg


		
class People(Connector):
	def __init__(self,msg,name):
		Connector.__init__(self,msg,name)
		self.pos_reply = Data().get_data()
		self.i = random.randint(0, len(self.pos_reply))
		self.j = 0

	def create_button(self,frame):
		def btn_func(self):
			cntor = Data(name_file_dict[self.index_name])
			self.pos_reply = cntor.get_data()
			self.i = random.randint(0, len(self.pos_reply))
			self.j = 0
			self.msg.cur_conn = self
		self.button = Button(frame.fra_cnt,text=self.reply_name,font=font,fg=fg_color,bg=bg_color,width=width,command=lambda:btn_func(self))

	def auto_reply(self):
		while self.i==self.j:
		  self.i = random.randint(0, len(self.pos_reply))
		self.j = self.i
		fin_msg = self.pos_reply[self.i]+'\n'
		return fin_msg



class MovieRecomm(People):
	def __init__(self,msg,name):
		People.__init__(self,msg,name)






