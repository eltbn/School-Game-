def gogo():
  score = 0
  loop = False
  import threading
  import pygame as p
  from random import randint
  import time

  BLACK = p.Color('#000000')
  WHITE = p.Color('#FFFFFF')
  RED = p.Color('#FF0000')

  p.init()
  window = p.display.set_mode((400,400))
  p.display.set_caption('EVANS FOR STATEMENT GAME')
  clock = p.time.Clock()

  text = 'Welcome to the dot game'
  entry = True
  def timer(t):
    while t:
      mins,secs = divmod(t,60)
      tiimer = '{:02d}:{:02d}'.format(mins,secs)
      time.sleep(1)
      t-=1 

  text1=''
  text2=''

  def ok(text):
    window.fill(BLACK)
    font=p.font.Font('freesansbold.ttf',16)
    board = font.render(f"{text} ",  True,WHITE)
    textrec = board.get_rect()
    textrec.center = (200,200)
    window.blit(board,textrec)
    p.display.update()


  ok('Welcome to the Dot Game')
  timer(3)
  ok('Click all the dots you can before time runs out!')
  timer(3)
  ok('The red square is your cursor!')
  timer(3)
  ok('You will have 15 seconds')
  timer(3)
  ok('Type start to start.')
  c=input()
  if c == 'start':
    loop = True
    start_time = time.process_time()


  def stop():
    stop.iscalled = True
    ok(f'Times up! Your score was {score}')
    p.display.update()
    timer(5)
    ok('If you would like to play type again')
    k = input()
    if k == 'again':
      return gogo()
    else:
      p.exit()
  stop.iscalled = False

  def timeleft(self):
    self = self-start_time
    lit = round(self,1)
    lit = lit*10
    font=p.font.Font('freesansbold.ttf',16)
    board = font.render(f"Time: {lit} ",  True,WHITE)
    textrec = board.get_rect()
    textrec.center = (50,30)
    window.blit(board,textrec)

  def scoreboard():
    k = p.font.Font('freesansbold.ttf',16)
    kk = k.render(f"Score:{score}",True,WHITE)
    pos = kk.get_rect()
    pos.center=(200,25)
    window.blit(kk,pos)

  class dot(p.sprite.Sprite):
    def __init__(self,width,height):
      super().__init__()
      self.image = p.Surface([width,height])
      p.draw.rect(self.image,WHITE,[0,0,width,height])
      self.rect = self.image.get_rect()
    
    def clicked(self):
      self.rect.x=randint(30,370)
      self.rect.y=randint(30,370)

  class cursor(p.sprite.Sprite):
    def __init__(self,width,height):
      super().__init__()
      self.image = p.Surface([width,height])
      p.draw.rect(self.image,RED,[0,0,width,height])
      self.rect = self.image.get_rect()

    def update(self):
      pos = p.mouse.get_pos()
      self.rect.midtop = pos

  moose = cursor(10,10)
  square = dot(30,30)
  square.rect.x = 170
  square.rect.y=170
  sprites = p.sprite.Group()
  sprites.add(square)
  sprites.add(moose)

  while loop:
    window.fill(BLACK)

    eventget = p.event.get()
    for event in eventget:
      if event.type == p.QUIT:
        start = False
      if event.type == p.MOUSEBUTTONUP and p.sprite.collide_mask(square,moose):
          score += 1
          square.clicked()

    aight = time.process_time()
    if aight > 1.5+start_time:
      stop()
    if stop.iscalled:
      break

    timeleft(aight)
    scoreboard() 
    clock.tick(60)
    sprites.update()
    sprites.draw(window)
    p.display.update()
    
if __name__ == '__main__':
  gogo()