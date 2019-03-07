class Connector:
	def __init(self):
		self.kind = ""
    	self.msg_for_url = ""
    	self.i = random.randint(0, len(self.pos_reply))
    	self.j = 0
		self.reply_name = u"皮皮熊"

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