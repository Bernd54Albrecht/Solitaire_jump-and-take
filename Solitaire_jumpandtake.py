#! /usr/bin/python3
# Solitaire - jump and take
# By Bernd54Albrecht@gmail.com
# Jürgen-Fuhlendorf-Schule, D-24576 Bad Bramstedt
# 29.02.2016
# Happy birthday, Raspberry Pi
# Welcome on board, RasPi3
# ---------------------------------------------------

import pygame, sys           #, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


SIZE=50
windowWidth = 9*SIZE
windowHeight = 9*SIZE
hot=False

pygame.init()
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Solitaire - jump and take')

board = {}

# Set up the images.
piece=pygame.image.load("Sol_piece.png")
piece_hot=pygame.image.load("Sol_piece_hot.png")
empty=pygame.image.load("Sol_empty.png")
outside=pygame.image.load("Sol_bg.png")

# Use smoothscale() to adjust the images:
piece = pygame.transform.smoothscale(piece, (SIZE,SIZE))
piece_hot = pygame.transform.smoothscale(piece_hot, (SIZE,SIZE))
empty = pygame.transform.smoothscale(empty, (SIZE,SIZE))
outside = pygame.transform.smoothscale(outside, (SIZE,SIZE))

mousePosition = None


def drawButtons():

  for POS in range(81):
    xPos=POS//9
    yPos=POS%9
    position=(xPos*SIZE,yPos*SIZE)
    surface.blit(board[POS], position)


def handle1Click():  # first click on valid piece

  global mousePosition, hot,selxPos, selyPos,POShot


  for POS in range(81):
    xPos=POS//9
    yPos=POS%9
    position=(xPos*SIZE,yPos*SIZE)

    if mousePosition[0] > position[0] and mousePosition[0] < position[0] + SIZE:

      if mousePosition[1] > position[1] and mousePosition[1] < position[1] + SIZE:
        (selxPos,selyPos)=(mousePosition[0]//SIZE,mousePosition[1]//SIZE)
#        print(selxPos,selyPos)
        if board[POS]==piece and hot==False and ((board[POS-1]==piece and board[POS-2]==empty) or (board[POS+1]==piece and board[POS+2]==empty) or (board[POS-9]==piece and board[POS-18]==empty) or (board[POS+9]==piece and board[POS+18]==empty)):   

          board[POS]=piece_hot
          POShot=POS
          hot=True
          
        else:
          print("not valid")
          

def handle2Click():  # second click on empty space   -   make the move

  global mousePosition, hot,sel2xPos, sel2yPos,POShot

  for POS in range(81):
    buttonSize = SIZE
    xPos=POS//9
    yPos=POS%9
    position=(xPos*SIZE,yPos*SIZE)

    if mousePosition[0] > position[0] and mousePosition[0] < position[0] + SIZE:

      if mousePosition[1] > position[1] and mousePosition[1] < position[1] + SIZE:
        (sel2xPos,sel2yPos)=(mousePosition[0]//SIZE,mousePosition[1]//SIZE)
#        print(sel2xPos,sel2yPos)
        if board[POS]==piece_hot and hot==True:
          board[POS]=piece
          hot=False


        if board[POS]==empty and POShot-POS==-2 and board[POS-1]==piece:
          board[POS]=piece
          board[POShot]=empty
          board[POS-1]=empty
          hot=False

        elif board[POS]==empty and POShot-POS==2 and board[POS+1]==piece:                             
          board[POS]=piece
          board[POShot]=empty
          board[POS+1]=empty
          hot=False

        elif board[POS]==empty and POShot-POS==-18 and board[POS-9]==piece:
                    
          board[POS]=piece
          board[POShot]=empty
          board[POS-9]=empty
          hot=False

        elif board[POS]==empty and POShot-POS==+18 and board[POS+9]==piece:                               
          
          board[POS]=piece
          board[POShot]=empty
          board[POS+9]=empty
          hot=False

          
        else:
          print("not valid")



def quitGame():
  pygame.quit()
  sys.exit()

# Create Buttons

board.update({ 0 : outside})
board.update({ 1 : outside})
board.update({ 2 : outside})
board.update({ 3 : outside})
board.update({ 4 : outside})
board.update({ 5 : outside})
board.update({ 6 : outside})
board.update({ 7 : outside})
board.update({ 8 : outside})

board.update({ 9 : outside})
board.update({ 10 : outside})
board.update({ 11 : outside})
board.update({ 12 : piece})
board.update({ 13 : piece})
board.update({ 14 : piece})
board.update({ 15 : outside})
board.update({ 16 : outside})
board.update({ 17 : outside})

board.update({ 18 : outside})
board.update({ 19 : outside})
board.update({ 20 : outside})
board.update({ 21 : piece})
board.update({ 22 : piece})
board.update({ 23 : piece})
board.update({ 24 : outside})
board.update({ 25 : outside})
board.update({ 26 : outside})

board.update({ 27 : outside})
board.update({ 28 : piece,})
board.update({ 29 : piece})
board.update({ 30 : piece})
board.update({ 31 : piece})
board.update({ 32 : piece})
board.update({ 33 : piece})
board.update({ 34 : piece})
board.update({ 35 : outside})

board.update({ 36 : outside})
board.update({ 37 : piece})
board.update({ 38 : piece})
board.update({ 39 : piece})
board.update({ 40 : empty})
board.update({ 41 : piece})
board.update({ 42 : piece})
board.update({ 43 : piece})
board.update({ 44 : outside})

board.update({ 45 : outside})
board.update({ 46 : piece})
board.update({ 47 : piece})
board.update({ 48 : piece})
board.update({ 49 : piece})
board.update({ 50 : piece})
board.update({ 51 : piece})
board.update({ 52 : piece})
board.update({ 53 : outside})

board.update({ 54 : outside})
board.update({ 55 : outside})
board.update({ 56 : outside})
board.update({ 57 : piece})
board.update({ 58 : piece})
board.update({ 59 : piece})
board.update({ 60 : outside})
board.update({ 61 : outside})
board.update({ 62 : outside})

board.update({ 63 : outside})
board.update({ 64 : outside})
board.update({ 65 : outside})
board.update({ 66 : piece})
board.update({ 67 : piece})
board.update({ 68 : piece})
board.update({ 69 : outside})
board.update({ 70 : outside})
board.update({ 71 : outside})

board.update({ 72 : outside})
board.update({ 73 : outside})
board.update({ 74 : outside})
board.update({ 75 : outside})
board.update({ 76 : outside})
board.update({ 77 : outside})
board.update({ 78 : outside})
board.update({ 79 : outside})
board.update({ 80 : outside})






# 'main' loop
while True:

  surface.fill((255,255,255))

  mousePosition = pygame.mouse.get_pos()

  for event in GAME_EVENTS.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_ESCAPE:
        quitGame()

    if event.type == GAME_GLOBALS.QUIT:
      quitGame()

    if event.type == pygame.MOUSEBUTTONUP:
      if hot==False:
        handle1Click()
      else:    
        handle2Click()

  drawButtons()


  pygame.display.update()
