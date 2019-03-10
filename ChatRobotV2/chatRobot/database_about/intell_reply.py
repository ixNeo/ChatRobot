import jieba
import sqlite3
import jieba.posseg as pseg
import random
file = 'text/李晓辰5.txt'
  # 从文件中得到数据，也可以自定义数据，包含数据处理，可以改进
# 以后：更加智能化的处理，精准的推荐
data = ['我明天要去上课','。。。你这是编程疯魔石乐志？','95后的新语言，我假装听不懂(/∇＼*),这个消息时间很迷啊，作息一如既往地稳，送来李开复的祝福,我猜你的汽构不在那40%（逃']


def process_data(f):
	sens = f.read().split('。')
	res = []
	flag = 0
	for sen in sens:
		sen = sen.strip(" ").strip("——").strip("——").replace(".","")
		senc = ""
		for c in sen:      
			if c.isdigit():
				pass
			else:
				senc += c
		res.append(senc)
	return res


def get_data(path):
	if path == "./text/poem.txt" or path =="./text/result.txt":
		f = open(path,'r',encoding='gbk')
	else:
		f = open(path,'r',encoding="utf-8")
	# 用处理过的数据
	# res = process_data(f)
	res = f.readlines()
	pos_reply=res+ [u'大宝贝你好',u"要开心呦",u"人家还是个孩子哩",u"然后呢",u"所以，你还要我怎样",u"不听不听，王八念经"]
	f.close()
	return pos_reply


# 得到（词，词性）列表
def get_posseg(sen,mode='list'):
	words = pseg.cut(sen)
	# for word, flag in words:
	# 	print('%s %s' % (word, flag))
	words = [word+'-'+flag for word,flag in words]
	return ','.join(words)


def create_table():
	conn = sqlite3.connect('origin_data.db')
	cursor = conn.cursor()
	cursor.execute('create table xiaochen_and_me (id integer primary key autoincrement,\
							time varchar(20), name varchar(20), sentence varchar(20),\
							word_list varchar(20))')
	cursor.execute('delete from xiaochen_and_me')
	f = open(file,'r',encoding="utf-8")
	sens = f.readlines()
	sens = [sen.strip() for sen in sens if sen!='\n']
	res = []
	name = ''
	time_sen = ''
	for sen in sens:
		if sen[0]=='2':
			time_sen = sen[:19]
			name = [c for c in sen if not c.isdigit() and c not in ['-',':',' ']]
			name =  ''.join(name)
			prename = name
			# print(name)
		else:	res.append((time_sen,name,sen,get_posseg(sen)))
	# print(res)
	for i in range(len(res)):
		tup = res[i]
		cursor.execute('insert into xiaochen_and_me (time, name, sentence,word_list) values (?,?,?,?)' ,tup)
	print(cursor.rowcount)
	cursor.close()
	conn.commit()
	conn.close()


def str2list(data):
	return data.split(',')


# 根据tanimoto距离度量进行评分，得到可能的输出，格式和数据库表中类似
def get_prob_list(my_input,all_output,pos):
	prob_list = []
	for word_list in all_output:
		score = 0
		word_list_split = str2list(word_list[pos])
		for word in word_list_split:
			if word in my_input:
				score += 1
		score = 1.0*score/(len(word_list_split)+len(my_input)-score)
		# score = 1.0*score/(len(word_list))
		prob_list.append((round(score,4),word_list_split,word_list[1],word_list[0]))
	prob_list.sort(reverse=True)
	return prob_list


# 分割句子中的词和词性，对构建以词性为key的字典，为后续的按照词性随机输出做准备
# res表示完整的句子；res_dict表示词性关联的字典
def get_prob_list_sen(prob_list):
	res = []
	res_dict = {}
	for score,sen,sen_com,ids in prob_list:
		res_sen = []
		for word in sen:
			word_essense = word.split('-')
			res_dict.setdefault(word_essense[1],[])
			res_dict[word_essense[1]].append(word_essense[0])
			res_sen.append(word_essense[0])
		# sen = [word.split('-')[0] for word in sen]
		res.append(''.join(res_sen))
	return res,res_dict

# 中间层。根据输入以及姓名查表，根据评分得到可能的输出
def get_part_prob_list(my_input,name):
	cursor.execute('select id, sentence, word_list from xiaochen_and_me where name=?',(name,))
	all_output = cursor.fetchall()
	prob_list = get_prob_list(my_input,all_output,2)
	return prob_list


# 随机输出函数。每一个词性都有一定的概率输出；若该词性输出，则从对应列表中随机输出。（两个随机）
def get_random_reply(res_dict,num):
	reply = ''
	for k,v in res_dict.items():
		if random.random()>num:
			reply = reply + random.choice(v)
	return reply


# solution 3
# 直接根据输入，和对方的所有输出进行距离计算，算出距离最小的。理论依据：对话的内容相关即可。之后可以根据词性进行混合
def get_output_base_content(my_input,mode='same'):
	prob_list = get_part_prob_list(my_input,'李晓辰')
	res,res_dict = get_prob_list_sen(prob_list[:3])
	print('res: ',res)
	if mode=='same':
		reply = res[random.randint(0,len(res)-1)]
	else:
		reply = get_random_reply(res_dict,0.2)
	# print('reply: ',reply)
	return reply


# solution 1
# 根据输入，先和自己的输入进行距离计算，找到近似输入；再用近似输入和对方的所有输出进行距离计算，算出距离最小的
def get_output_base_essense(my_input):
	prob_list = get_part_prob_list(my_input,'ixneo')
	# print('input-simpliy: ', prob_list[:3])
	# print('*'*50)
	reply_sum = []
	for score,sen_list,sen_com,ids in prob_list[:3]:
		cursor.execute('select id,sentence,word_list from xiaochen_and_me where name=? and id>?',('李晓辰',ids))
		all_output = cursor.fetchall()
		prob_list = get_prob_list(my_input,all_output,2)
		res ,res_dict= get_prob_list_sen(prob_list[:3])
		reply = ''
		reply = get_random_reply(res_dict,0.5)
		# print('reply: ',reply)
		reply_sum.append(reply)
	return reply_sum[random.randint(0,2)]


if __name__=="__main__":
	# get_output_base_content()
	my_input = "我宅的太久了"
	my_input = get_posseg(my_input)
	my_input = str2list(my_input)
	conn = sqlite3.connect('origin_data.db')
	cursor = conn.cursor()

	reply= get_output_base_essense(my_input)
	print(reply)
	cursor.close()
	conn.close()

