# 项目简介

1. 用python3实现的多功能机器人，可以实现中英互译、电影推荐、个性化机器人陪聊、音乐播放、头像展示等功能
2. 具体：
3. （项目亮点）好友联系人：爬取并清洗个人QQ消息记录或者电影台词，数据库存储即时消息记录，设计智能回复算法。涉及jieba分词，自然语言处理相关内容
4. 机器人Alice陪聊/中英互译功能：调用图灵机器人/网易翻译官方API
5. 电影推荐：爬取豆瓣电影TOP250数据

[详情/迭代过程/开发重难点: 见博客地址](https://ixneo.github.io/2019/03/10/chatbolt/)

# 重难点概览（已解决）
### 1. windows系统 ==> manjaro-linux系统的移植

- 中文字体显示问题
### 2. 硬编码 ==> 批量操作/自动化
- 抽象出Conn类（联系人类），并对派生类重载函数。利用多态简化结构。进一步理解类和对象的区别
> 黑魔法：eval()/locals()/global()函数。（已尝试，效果不如上述方法）

### 3. 数据库操作 & 智能回复算法设计
  - 方案一（已实现）：对输入分词，找到和先验输入的距离，根据距离前几的输出以及词性，进行混合输出（每个词性中随机挑选某个输入）。
        - 难点：灵活度很大，一句话的组成成分很复杂，可以是动宾短语，可以是整句。词性的组合是难点。
        - 理论依据：根据现实中对方的应答，做出回复
        - 此处对所有词性的顺序打乱，是否输出按照概率，输出哪一个词按照概率。没有考虑具体如何成句（考虑到网上聊天的随意性，好像此处假设合理）
  - 方案二（不合适）：数据库预处理，得到新表。对得到的输出句子的重复数目进行统计，挑选前几名，根据词性进行混合
  - 方案三（已实现）：直接根据输入，和对方的所有输出进行距离计算，算出距离最小的。理论依据：对话的内容相关即可。之后可以根据词性进行混合
      - 只能在原有的输出中原样输出
      > #### 问题
      > 真实的聊天记录不是问答式的，不是单向的，在整个上下文中，问答角色的确立是模糊的。所以很难根据输入确定输出。直接按照名字和话语列表为一行，然后按照周围的其他角色当做回复
      >
      > #### 后续研究方向
      > 一个句子的构成是多种多样的，可以由不同类型以及不同顺序的词性构成，但又存在顺序规律，不是完全随机的。需要在几个固定模式下进行随机，效果会更好。未考虑相邻词的联系
# 文件目录结构

chatRobot
|--main.py    # 运行图形界面程序
|--class_ui.py    # UI类。用于frame的规划以及绘制
|--class_msg.py    # Msg类。用于整个收发消息流程的控制。
|--class_conn_people.py    # Conn类以及其派生类。每个联系人有独特的自动回复功能和专属的按钮
|--class_data.py    # Data类. 用于清洗以及读取数据
|--class_music.py    # Music类。用于音乐播放暂停的控制，借助pygame库
|--const_data.py    # 数据常量的存储
|--get_movie_data.py    # 爬虫程序。用于爬取豆瓣电影文件
|--mess.py    # 垃圾桶，用于写demo
|--text    # .txt文件。存储消息记录以及爬取得到的数据
|--image    # 图片资源
|--music    # 音乐资源
|--database-about    # 数据库以及算法设计的demo
	|--intell_reply.py    # 可以运行。选取text中的特定文件进行测试，三种算法方案均能正确运行。内含数据库建表等操作，如需更换数据源，需要再次调用create_table()函数
 	|--origin_data.db   # 数据库文件
	|--text    # 文本资源

# ChatRobot

## introduce

one chatting robot can broadcasting music and reply automatically

## basic function

#### on the chatting window, you can send message to the robot which can reply you automaticly.

#### including kinds of robots which based on the .txt file

1. on which step, we can edit the txt file and process the file to make the robot's brain more smart, so that it can reply more intelligently
2. on the left column, u can choose different style of robot u want to talk, and this is based on multifiles.
3. on this document, I got materials including QQ chat record, poems and movie scripts. u can add something else.

#### music playing

1. a short sound will appear once u press the <L_control> or the "发送"
2. at the bottom of the main window, u can choose to play, pause, stop the background music which is just one song.

```
p.s. when u choose to play background music, the sound noticing won't appear, u have to stop the music, but not pause, the sound will work normally again.
```

#### image.

1. on the right column, there is a picture to decorate the window. 

## how to use

1. run main.py to start the chatting window
2. choose a specific style robot u want to chat with on the left column.
3. on the bottom, u can choose to start, pause, stop the background music.
4. then, u can type sentence in the bottom subwindow, press button "发送" or hot-key <L_control> to send the message
5. once u send the message, the top left sub_window will show your message record, while the top right subwindow will show the robot's reply

## environment

win10, python3.6.3

## package support

1. tkinter
2. pygame
3. PIL
4. jieba
