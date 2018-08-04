import pygame
import time
import random

class Music:

  switch_on = True

  def __init__(self,filename="./music/cuan.mp3"):
    
    self.filename = filename
    self.start_bool = True
    pygame.mixer.init()

  def msg_sound(self):

    filename = self.filename.encode("UTF-8")
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(0,0.2)

  def bg_sound(self):
    
    if self.start_bool==True:
      filename = self.filename.encode("UTF-8")
      
      pygame.mixer.music.load(filename)
      pygame.mixer.music.play(0,0.2)
      self.start_bool = False
    else:
      pygame.mixer.music.unpause()

  def track_pause(self):

    pygame.mixer.music.pause()


  def track_stop(self):

    pygame.mixer.music.stop()
    self.start_bool=True