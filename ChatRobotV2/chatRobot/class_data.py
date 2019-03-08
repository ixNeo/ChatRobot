class Data:
  # 从文件中得到数据，也可以自定义数据，包含数据处理，可以改进
# 以后：更加智能化的处理，精准的推荐

  def __init__(self,p="./text/xiongchuyuan.txt"):
    self.path = p

  def process_data(self,f):
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


  def get_data(self):
    if self.path == "./text/poem.txt" or self.path =="./text/result.txt":
      f = open(self.path,'r',encoding='gbk')
    else:
      f = open(self.path,'r',encoding="utf-8")
    # 用处理过的数据
    # res = process_data(f)
    res = f.readlines()
    pos_reply=res+ [u'大宝贝你好',u"要开心呦",u"人家还是个孩子哩",u"然后呢",u"所以，你还要我怎样",u"不听不听，王八念经"]
    f.close()
    self.pos_reply = pos_reply
    return pos_reply