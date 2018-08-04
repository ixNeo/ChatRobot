# 中文注解
1. 用python3实现的多功能机器人，可以实现中英互译、电影推荐、个性化机器人陪聊、音乐播放、头像展示等功能
    1. 翻译功能：调用网易翻译的API
    2. 机器人Alice陪聊：调用图灵机器人API
    3. 电影推荐：爬取豆瓣TOP250数据
    4. 其余联系人：爬取个人QQ消息记录或者电影台词，随机生成


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
  p.s. when u choose to play background music, the sound noticing won't appear, u have to stop the music, but not pause, the sound will work normally again.
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

## work not to do
  1. more intelligent reply. Because there just time random, which is not really smart. u can improve it by deep learning.
  2. more songs support. u can add functions like "next songs"
  3. more images. u can add the button to change the picture.
  

