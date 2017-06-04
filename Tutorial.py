#Ryan Edelstein
#My first attempt at pygame; simple program

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000, 500), 32)
pygame.display.set_caption('Game #1')

FPS = 60  #controls the speed at which the cat moves on the page
fpsClock = pygame.time.Clock() #tracks the speed

BLACK = (0, 0, 0) #initializes the color black
WHITE = (255, 255, 255) #initializes the color white
RED = (255, 0, 0) # initializes rgb
GREEN = (0, 255, 0)
BLUE = (0,0, 255)

catImg = pygame.image.load('cat.png' ) #import cat png from local files
catx = 10
caty = 10

direction = 'right' #declares direction as right


while True:  # main game loop
  DISPLAYSURF.fill(WHITE) #fills the background as white
  if direction == 'right': #checks the direction of the movement
      catx += 5            #increases the x value by 5 pixels
      if catx == 280:      #if the x value is equal to 200, change direction to down.
          direction = 'down'
  elif direction == 'down':
      caty += 5
      if caty == 220:
          direction = 'left'
  elif direction == 'left':
      catx -= 5
      if catx == 10:
          direction = 'up'
  elif direction == 'up':
      caty -= 5
      if caty == 10:
          direction = 'right'
  DISPLAYSURF.blit(catImg, (catx, caty)) #displays the cat image
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
  fpsClock.tick(FPS)
