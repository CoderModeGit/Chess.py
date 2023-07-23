import math
import pygame
from pygame import mixer
from pygame.locals import*
programIcon = pygame.image.load("Images/Icon.png")
boardimg = pygame.image.load("Images/board.jpeg")
title = pygame.image.load("Images/Menu/Title.jpeg")
button = pygame.image.load("Images/Menu/Button.jpeg")
buttonselect = pygame.image.load("Images/Menu/ButtonSelected.jpeg")
menugui = pygame.image.load("Images/Menu/Gui.jpeg")
vsgui = pygame.image.load("Images/Menu/VS.jpeg")
intrologo = pygame.image.load("Images/Menu/intrologo.jpeg")
black = (0, 0, 0)
w = 1000
h = 700
screen = pygame.display.set_mode((w, h))
introsurface = pygame.Surface((w,h),pygame.SRCALPHA)
screen.fill((black))
running = 1 #If the program is running
movementx = 0
movementy = 0
SelectedPiece = "None" #The current selected piece 
piece_x = 0
piece_y = 0
Start_x = 0
Start_y = 0
canmove = [] #List of all possible moves for a piece
personalcanmove = [] #Canmove, but filtered
player1 = "Player" #Name of Player1
player2 = "Bot" #Name of Player2
showgreenthing = True #If to show a green sqaure where your mouse is
lastselectpiece = "None" #The last selected piece, cannot be "None"
introtimer = 400 #The amount of time for the intro
coords = ["a","b","c","d","e","f","g","h"]

mixer.init()
mixer.music.load("Sound/Enough_Plucks.wav")
  
#
mixer.music.set_volume(0.7)

board = [
    "RookB","KnightB","BishopB","QueenB","KingB","BishopB","KnightB","RookB",
    "PawnB","PawnB","PawnB","PawnB","PawnB","PawnB","PawnB","PawnB",
    "None","None","None","None","None","None","None","None",
    "None","None","None","None","None","None","None","None",
    "None","None","None","None","None","None","None","None",
    "None","None","None","None","None","None","None","None",
    "PawnW","PawnW","PawnW","PawnW","PawnW","PawnW","PawnW","PawnW",
    "RookW","KnightW","BishopW","QueenW","KingW","BishopW","KnightW","RookW",
]
def loadpiece(X,Y,Piece,IsMovingPiece):
    if Piece != "None" and Piece != None: 
        if IsMovingPiece:
            screen.blit(pygame.image.load("Images/Pieces/" + str(Piece) + ".jpeg"),((int(X) * 75)+ 200 + movementx,(int(Y) * 75)+ 60 + movementy)) #Get image file name from Piece, and x/y
        else: 
            screen.blit(pygame.image.load("Images/Pieces/" + str(Piece) + ".jpeg"),((int(X) * 75)+ 200,(int(Y) * 75)+ 60)) #Get image file name from Piece, and x/y
def loadpieces():
    for i in range(len(board)): #For every piece on the board
        if i // 8 == 7 and board[i] == "PawnB": 
            board[i] = "QueenB"                   #If pawn makes it to other side of board, promoted to queen
        elif i // 8 == 0 and board[i] == "PawnW":
            board[i] = "QueenW"
        loadpiece(i % 8, i // 8, board[i],False) #Find x and y from index, show piece on board
def getpieceat(PieceX,PieceY):
    pieceindex = (int(8 * PieceY) + (int(PieceX) - 1))
    if pieceindex > -1 and pieceindex < 64:
       return str(board[int(pieceindex)])
    else:
        return "None"
def canmovepiece(piece_x,piece_y,canmove):
    return str(piece_x) + "," + str(piece_y) in canmove
def inrange(piece_x,piece_y):
    if piece_x > 0 and piece_x < 9 and piece_y > -1 and piece_y < 8:
          return True
    else:
          return False
def showcanmove(personalcanmove):
    for i in personalcanmove:
        x = int(str(i).split(",")[0]) - 1 
        y = int(str(i).split(",")[1])
        loadpiece(x,y,"CanMove",False)
def handlemovement(Start_x,Start_y,SelectedPiece,board):
    if SelectedPiece == "PawnW":
            if Start_y == 6 and board[8* (Start_y - 2) + (Start_x - 1)] == "None":
                canmove.append(str(Start_x) + "," + str(Start_y - 2))
            if board[8* (Start_y - 1) + (Start_x - 1)] == "None":
                canmove.append(str(Start_x) + "," + str(Start_y - 1))
            if board[8* (Start_y - 1) + (Start_x - 2)][-1] == "B":
              canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
            if board[8* (Start_y - 1) + (Start_x)][-1] == "B":
              canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
    elif SelectedPiece == "KingW":
          if getpieceat(Start_x + 1,Start_y) == "None" or getpieceat(Start_x + 1,Start_y)[-1] == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y))
          if getpieceat(Start_x - 1,Start_y) == "None" or getpieceat(Start_x - 1,Start_y)[-1] == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y))
          if getpieceat(Start_x + 1,Start_y) == "None" or getpieceat(Start_x + 1,Start_y)[-1] == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x - 1,Start_y + 1) == "None" or getpieceat(Start_x - 1,Start_y + 1)[-1] == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x + 1,Start_y - 1) == "None" or getpieceat(Start_x + 1,Start_y - 1)[-1] == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y -1))
          if getpieceat(Start_x - 1,Start_y - 1) == "None" or getpieceat(Start_x - 1,Start_y - 1)[-1] == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x,Start_y + 1) == "None" or getpieceat(Start_x,Start_y + 1)[-1] == "B":
           canmove.append(str(Start_x) + "," + str(Start_y + 1))
          if getpieceat(Start_x,Start_y - 1) == "None" or getpieceat(Start_x,Start_y - 1)[-1] == "B":
           canmove.append(str(Start_x) + "," + str(Start_y - 1))
    elif SelectedPiece == "RookW":
                if getpieceat(Start_x + 1, Start_y)[-1]  == "B":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
                elif getpieceat(Start_x + 1, Start_y) == "None":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
                    if getpieceat(Start_x + 2, Start_y)[-1]  == "B":
                          canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                    elif getpieceat(Start_x + 2, Start_y) == "None":
                        canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                        if getpieceat(Start_x + 3, Start_y)[-1]  == "B":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                        elif getpieceat(Start_x + 3, Start_y) == "None":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                           if getpieceat(Start_x + 4, Start_y)[-1]  == "B":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                           elif getpieceat(Start_x + 4, Start_y) == "None":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                              if getpieceat(Start_x + 5, Start_y)[-1]  == "B":
                                canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                              elif getpieceat(Start_x + 5, Start_y) == "None":
                                 canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                                 if getpieceat(Start_x + 6, Start_y)[-1]  == "B":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                 elif getpieceat(Start_x + 6, Start_y) == "None":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x + 7, Start_y)[-1]  == "B":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x + 7, Start_y) == "None":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                      if getpieceat(Start_x + 8, Start_y)[-1]  == "B":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
                                      elif getpieceat(Start_x + 8, Start_y) == "None":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
                if getpieceat(Start_x, Start_y + 1)[-1] == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
                elif getpieceat(Start_x, Start_y + 1) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
                   if getpieceat(Start_x, Start_y + 2)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                   elif getpieceat(Start_x, Start_y + 2) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                      if getpieceat(Start_x, Start_y + 3)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                      elif getpieceat(Start_x, Start_y + 3) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                         if getpieceat(Start_x, Start_y + 4)[-1]  == "B":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                         elif getpieceat(Start_x, Start_y + 4) == "None":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                             if getpieceat(Start_x, Start_y + 5)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                             elif getpieceat(Start_x, Start_y + 5) == "None":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                                if getpieceat(Start_x, Start_y + 6)[-1]  == "B":
                                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                elif getpieceat(Start_x, Start_y + 6) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                  if getpieceat(Start_x, Start_y + 7)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                  elif getpieceat(Start_x, Start_y + 7) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                     if getpieceat(Start_x, Start_y + 8)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
                                     elif getpieceat(Start_x, Start_y + 8) == "None":
                                       canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
                if getpieceat(Start_x, Start_y - 1)[-1]  == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
                elif getpieceat(Start_x, Start_y - 1) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
                   if getpieceat(Start_x, Start_y - 2)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                   elif getpieceat(Start_x, Start_y - 2) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                      if getpieceat(Start_x, Start_y - 3)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                      elif getpieceat(Start_x, Start_y - 3) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                         if getpieceat(Start_x, Start_y - 4)[-1]  == "B":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                         elif getpieceat(Start_x, Start_y - 4) == "None":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                            if getpieceat(Start_x, Start_y - 5)[-1]  == "B":
                              canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                            elif getpieceat(Start_x, Start_y - 5) == "None":
                               canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                               if getpieceat(Start_x, Start_y - 6)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                               elif getpieceat(Start_x, Start_y - 6) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                                  if getpieceat(Start_x, Start_y - 7)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + -6))
                                  elif getpieceat(Start_x, Start_y - 7) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + -7))
                                     if getpieceat(Start_x, Start_y - 8)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
                                     elif getpieceat(Start_x, Start_y - 8) == "None":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
                if getpieceat(Start_x - 1,Start_y)[-1] == "B":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
                elif getpieceat(Start_x - 1,Start_y) == "None":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
                   if getpieceat(Start_x - 2,Start_y)[-1] == "B":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                   elif getpieceat(Start_x - 2,Start_y) == "None":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                      if getpieceat(Start_x - 3,Start_y)[-1] == "B":
                        canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                      elif getpieceat(Start_x - 3,Start_y) == "None":
                         canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                         if getpieceat(Start_x - 4,Start_y)[-1] == "B":
                           canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                         elif getpieceat(Start_x - 4,Start_y) == "None":
                            canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                            if getpieceat(Start_x - 5,Start_y)[-1] == "B":
                               canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                            elif getpieceat(Start_x - 5,Start_y) == "None":
                                canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                                if getpieceat(Start_x - 6,Start_y)[-1] == "B":
                                   canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                elif getpieceat(Start_x - 6,Start_y) == "None":
                                    canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x - 7,Start_y)[-1] == "B":
                                      canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x - 7,Start_y) == "None":
                                       canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                       if getpieceat(Start_x - 8,Start_y)[-1] == "B":
                                         canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
                                       elif getpieceat(Start_x - 8,Start_y) == "None":
                                          canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
    elif SelectedPiece == "KnightW":
       if getpieceat(Start_x - 1,Start_y + 2) == "None" or getpieceat(Start_x + 1,Start_y + 2)[-1] == "B":
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 2))
       if getpieceat(Start_x - 1,Start_y - 2) == "None" or getpieceat(Start_x - 1,Start_y - 2)[-1] == "B":
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 2))
       if getpieceat(Start_x - 1,Start_y + 2) == "None" or getpieceat(Start_x - 1,Start_y + 2)[-1] == "B":
          canmove.append(str(Start_x + -1) + "," + str(Start_y + 2))
       if getpieceat(Start_x - 1,Start_y - 2) == "None" or getpieceat(Start_x + 1,Start_y - 2)[-1] == "B":
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 2))
       if getpieceat(Start_x + 2,Start_y - 1) == "None" or getpieceat(Start_x + 2,Start_y - 1)[-1] == "B":
          canmove.append(str(Start_x + 2) + "," + str(Start_y - 1))
       if getpieceat(Start_x - 2,Start_y - 1) == "None" or getpieceat(Start_x - 2,Start_y - 1)[-1] == "B":
          canmove.append(str(Start_x - 2) + "," + str(Start_y - 1))
       if getpieceat(Start_x + 2,Start_y + 1) == "None" or getpieceat(Start_x + 2,Start_y + 1)[-1] == "B":
          canmove.append(str(Start_x + 2) + "," + str(Start_y + 1))
       if getpieceat(Start_x - 2,Start_y + 1) == "None" or getpieceat(Start_x - 2,Start_y + 1)[-1] == "B":
          canmove.append(str(Start_x - 2) + "," + str(Start_y + 1))         
    elif SelectedPiece == "BishopW":
       if getpieceat(Start_x - 1, Start_y - 1)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
       elif getpieceat(Start_x - 1, Start_y - 1) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x - 2, Start_y - 2)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x - 2, Start_y - 2) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x - 3, Start_y - 3)[-1]  == "B":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x - 3, Start_y - 3) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x - 4, Start_y - 4)[-1]  == "B":
                    canmove.append(str(Start_x + -4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x - 4, Start_y - 4) == "None":
                  canmove.append(str(Start_x + -4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x - 5, Start_y - 5)[-1]  == "B":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x - 5, Start_y - 5) == "None":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x - 6, Start_y - 6)[-1]  == "B":
                     canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y - 6) == "None":
                      canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x - 7, Start_y - 7)[-1]  == "B":
                        canmove.append(str(Start_x + -7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x - 7, Start_y - 7) == "None":
                          canmove.append(str(Start_x + -7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x - 8, Start_y - 8)[-1]  == "B":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x - 8, Start_y - 8) == "None":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
       if getpieceat(Start_x + 1, Start_y + 1)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
       elif getpieceat(Start_x + 1, Start_y + 1) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x + 2, Start_y + 2)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x + 2, Start_y + 2) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x + 3, Start_y + 3)[-1]  == "B":
                canmove.append(str(Start_x +  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x + 3, Start_y + 3) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x + 4, Start_y + 4)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x + 4, Start_y + 4) == "None":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x + 5, Start_y + 5)[-1]  == "B":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x + 5, Start_y + 5) == "None":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x + 6, Start_y + 6)[-1]  == "B":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x + 6, Start_y + 6) == "None":
                       canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x + 7, Start_y + 7)[-1]  == "B":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x + 7, Start_y + 7) == "None":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x + 8, Start_y + 8)[-1]  == "B":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x + 8, Start_y + 8) == "None":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
       if getpieceat(Start_x + 1, Start_y - 1)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
       elif getpieceat(Start_x + 1, Start_y - 1) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x + 2, Start_y - 2)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x + 2, Start_y - 2) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x + 3, Start_y - 3)[-1]  == "B":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x + 3, Start_y - 3) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x + 4, Start_y - 4)[-1]  == "B":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x + 4, Start_y - 4) == "None":
                  canmove.append(str(Start_x + 4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x + 5, Start_y - 5)[-1]  == "B":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x + 5, Start_y - 5) == "None":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x + 6, Start_y - 6)[-1]  == "B":
                     canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y + 6) == "None":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x + 7, Start_y - 7)[-1]  == "B":
                        canmove.append(str(Start_x + 7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x + 7, Start_y - 7) == "None":
                          canmove.append(str(Start_x + 7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x + 8, Start_y - 8)[-1]  == "B":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x + 8, Start_y - 8) == "None":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
       if getpieceat(Start_x - 1, Start_y + 1)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
       elif getpieceat(Start_x - 1, Start_y + 1) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x - 2, Start_y + 2)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x - 2, Start_y + 2) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x - 3, Start_y + 3)[-1]  == "B":
                canmove.append(str(Start_x -  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x - 3, Start_y + 3) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x - 4, Start_y + 4)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x - 4, Start_y + 4) == "None":
                    canmove.append(str(Start_x - 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x - 5, Start_y + 5)[-1]  == "B":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x - 5, Start_y + 5) == "None":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x - 6, Start_y + 6)[-1]  == "B":
                      canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x - 6, Start_y + 6) == "None":
                       canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x - 7, Start_y + 7)[-1]  == "B":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x - 7, Start_y + 7) == "None":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x - 8, Start_y + 8)[-1]  == "B":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x - 8, Start_y + 8) == "None":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
    elif SelectedPiece == "QueenW": 
         if getpieceat(Start_x - 1, Start_y - 1)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
         elif getpieceat(Start_x - 1, Start_y - 1) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x - 2, Start_y - 2)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x - 2, Start_y - 2) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x - 3, Start_y - 3)[-1]  == "B":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x - 3, Start_y - 3) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x - 4, Start_y - 4)[-1]  == "B":
                    canmove.append(str(Start_x + -4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x - 4, Start_y - 4) == "None":
                  canmove.append(str(Start_x + -4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x - 5, Start_y - 5)[-1]  == "B":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x - 5, Start_y - 5) == "None":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x - 6, Start_y - 6)[-1]  == "B":
                     canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y - 6) == "None":
                      canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x - 7, Start_y - 7)[-1]  == "B":
                        canmove.append(str(Start_x + -7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x - 7, Start_y - 7) == "None":
                          canmove.append(str(Start_x + -7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x - 8, Start_y - 8)[-1]  == "B":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x - 8, Start_y - 8) == "None":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
         if getpieceat(Start_x + 1, Start_y + 1)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
         elif getpieceat(Start_x + 1, Start_y + 1) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x + 2, Start_y + 2)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x + 2, Start_y + 2) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x + 3, Start_y + 3)[-1]  == "B":
                canmove.append(str(Start_x +  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x + 3, Start_y + 3) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x + 4, Start_y + 4)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x + 4, Start_y + 4) == "None":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x + 5, Start_y + 5)[-1]  == "B":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x + 5, Start_y + 5) == "None":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x + 6, Start_y + 6)[-1]  == "B":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x + 6, Start_y + 6) == "None":
                       canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x + 7, Start_y + 7)[-1]  == "B":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x + 7, Start_y + 7) == "None":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x + 8, Start_y + 8)[-1]  == "B":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x + 8, Start_y + 8) == "None":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
         if getpieceat(Start_x + 1, Start_y - 1)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
         elif getpieceat(Start_x + 1, Start_y - 1) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x + 2, Start_y - 2)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x + 2, Start_y - 2) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x + 3, Start_y - 3)[-1]  == "B":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x + 3, Start_y - 3) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x + 4, Start_y - 4)[-1]  == "B":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x + 4, Start_y - 4) == "None":
                  canmove.append(str(Start_x + 4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x + 5, Start_y - 5)[-1]  == "B":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x + 5, Start_y - 5) == "None":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x + 6, Start_y - 6)[-1]  == "B":
                     canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y + 6) == "None":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x + 7, Start_y - 7)[-1]  == "B":
                        canmove.append(str(Start_x + 7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x + 7, Start_y - 7) == "None":
                          canmove.append(str(Start_x + 7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x + 8, Start_y - 8)[-1]  == "B":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x + 8, Start_y - 8) == "None":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
         if getpieceat(Start_x - 1, Start_y + 1)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
         elif getpieceat(Start_x - 1, Start_y + 1) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x - 2, Start_y + 2)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x - 2, Start_y + 2) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x - 3, Start_y + 3)[-1]  == "B":
                canmove.append(str(Start_x -  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x - 3, Start_y + 3) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x - 4, Start_y + 4)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x - 4, Start_y + 4) == "None":
                    canmove.append(str(Start_x - 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x - 5, Start_y + 5)[-1]  == "B":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x - 5, Start_y + 5) == "None":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x - 6, Start_y + 6)[-1]  == "B":
                      canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x - 6, Start_y + 6) == "None":
                       canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x - 7, Start_y + 7)[-1]  == "B":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x - 7, Start_y + 7) == "None":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x - 8, Start_y + 8)[-1]  == "B":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x - 8, Start_y + 8) == "None":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
         if getpieceat(Start_x + 1, Start_y)[-1]  == "B":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
         elif getpieceat(Start_x + 1, Start_y) == "None":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
                    if getpieceat(Start_x + 2, Start_y)[-1]  == "B":
                          canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                    elif getpieceat(Start_x + 2, Start_y) == "None":
                        canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                        if getpieceat(Start_x + 3, Start_y)[-1]  == "B":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                        elif getpieceat(Start_x + 3, Start_y) == "None":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                           if getpieceat(Start_x + 4, Start_y)[-1]  == "B":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                           elif getpieceat(Start_x + 4, Start_y) == "None":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                              if getpieceat(Start_x + 5, Start_y)[-1]  == "B":
                                canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                              elif getpieceat(Start_x + 5, Start_y) == "None":
                                 canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                                 if getpieceat(Start_x + 6, Start_y)[-1]  == "B":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                 elif getpieceat(Start_x + 6, Start_y) == "None":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x + 7, Start_y)[-1]  == "B":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x + 7, Start_y) == "None":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                      if getpieceat(Start_x + 8, Start_y)[-1]  == "B":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
                                      elif getpieceat(Start_x + 8, Start_y) == "None":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
         if getpieceat(Start_x, Start_y + 1)[-1] == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
         elif getpieceat(Start_x, Start_y + 1) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
                   if getpieceat(Start_x, Start_y + 2)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                   elif getpieceat(Start_x, Start_y + 2) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                      if getpieceat(Start_x, Start_y + 3)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                      elif getpieceat(Start_x, Start_y + 3) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                         if getpieceat(Start_x, Start_y + 4)[-1]  == "B":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                         elif getpieceat(Start_x, Start_y + 4) == "None":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                             if getpieceat(Start_x, Start_y + 5)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                             elif getpieceat(Start_x, Start_y + 5) == "None":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                                if getpieceat(Start_x, Start_y + 6)[-1]  == "B":
                                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                elif getpieceat(Start_x, Start_y + 6) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                  if getpieceat(Start_x, Start_y + 7)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                  elif getpieceat(Start_x, Start_y + 7) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                     if getpieceat(Start_x, Start_y + 8)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
                                     elif getpieceat(Start_x, Start_y + 8) == "None":
                                       canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
         if getpieceat(Start_x, Start_y - 1)[-1]  == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
         elif getpieceat(Start_x, Start_y - 1) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
                   if getpieceat(Start_x, Start_y - 2)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                   elif getpieceat(Start_x, Start_y - 2) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                      if getpieceat(Start_x, Start_y - 3)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                      elif getpieceat(Start_x, Start_y - 3) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                         if getpieceat(Start_x, Start_y - 4)[-1]  == "B":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                         elif getpieceat(Start_x, Start_y - 4) == "None":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                            if getpieceat(Start_x, Start_y - 5)[-1]  == "B":
                              canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                            elif getpieceat(Start_x, Start_y - 5) == "None":
                               canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                               if getpieceat(Start_x, Start_y - 6)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                               elif getpieceat(Start_x, Start_y - 6) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                                  if getpieceat(Start_x, Start_y - 7)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + -6))
                                  elif getpieceat(Start_x, Start_y - 7) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + -7))
                                     if getpieceat(Start_x, Start_y - 8)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
                                     elif getpieceat(Start_x, Start_y - 8) == "None":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
         if getpieceat(Start_x - 1,Start_y)[-1] == "B":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
         elif getpieceat(Start_x - 1,Start_y) == "None":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
                   if getpieceat(Start_x - 2,Start_y)[-1] == "B":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                   elif getpieceat(Start_x - 2,Start_y) == "None":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                      if getpieceat(Start_x - 3,Start_y)[-1] == "B":
                        canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                      elif getpieceat(Start_x - 3,Start_y) == "None":
                         canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                         if getpieceat(Start_x - 4,Start_y)[-1] == "B":
                           canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                         elif getpieceat(Start_x - 4,Start_y) == "None":
                            canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                            if getpieceat(Start_x - 5,Start_y)[-1] == "B":
                               canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                            elif getpieceat(Start_x - 5,Start_y) == "None":
                                canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                                if getpieceat(Start_x - 6,Start_y)[-1] == "B":
                                   canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                elif getpieceat(Start_x - 6,Start_y) == "None":
                                    canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x - 7,Start_y)[-1] == "B":
                                      canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x - 7,Start_y) == "None":
                                       canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                       if getpieceat(Start_x - 8,Start_y)[-1] == "B":
                                         canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
                                       elif getpieceat(Start_x - 8,Start_y) == "None":
                                          canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
def handlemovementenemy(Start_x,Start_y,SelectedPiece,board):
    if SelectedPiece == "PawnW":
            if Start_y == 2 and board[8* (Start_y + 2) + (Start_x - 1)] == "None":
                canmove.append(str(Start_x) + "," + str(Start_y + 2))
            if board[8* (Start_y + 1) + (Start_x - 1)] == "None":
                canmove.append(str(Start_x) + "," + str(Start_y - 1))
            if board[8* (Start_y + 1) + (Start_x - 2)][-1] == "W":
              canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
            if board[8* (Start_y + 1) + (Start_x)][-1] == "W":
              canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
    elif SelectedPiece == "KingW":
          if getpieceat(Start_x + 1,Start_y) == "None" or getpieceat(Start_x + 1,Start_y)[-1] == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y))
          if getpieceat(Start_x - 1,Start_y) == "None" or getpieceat(Start_x - 1,Start_y)[-1] == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y))
          if getpieceat(Start_x + 1,Start_y) == "None" or getpieceat(Start_x + 1,Start_y)[-1] == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x - 1,Start_y + 1) == "None" or getpieceat(Start_x - 1,Start_y + 1)[-1] == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x + 1,Start_y - 1) == "None" or getpieceat(Start_x + 1,Start_y - 1)[-1] == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y -1))
          if getpieceat(Start_x - 1,Start_y - 1) == "None" or getpieceat(Start_x - 1,Start_y - 1)[-1] == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x,Start_y + 1) == "None" or getpieceat(Start_x,Start_y + 1)[-1] == "B":
           canmove.append(str(Start_x) + "," + str(Start_y + 1))
          if getpieceat(Start_x,Start_y - 1) == "None" or getpieceat(Start_x,Start_y - 1)[-1] == "B":
           canmove.append(str(Start_x) + "," + str(Start_y - 1))
    elif SelectedPiece == "RookW":
                if getpieceat(Start_x + 1, Start_y)[-1]  == "B":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
                elif getpieceat(Start_x + 1, Start_y) == "None":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
                    if getpieceat(Start_x + 2, Start_y)[-1]  == "B":
                          canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                    elif getpieceat(Start_x + 2, Start_y) == "None":
                        canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                        if getpieceat(Start_x + 3, Start_y)[-1]  == "B":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                        elif getpieceat(Start_x + 3, Start_y) == "None":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                           if getpieceat(Start_x + 4, Start_y)[-1]  == "B":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                           elif getpieceat(Start_x + 4, Start_y) == "None":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                              if getpieceat(Start_x + 5, Start_y)[-1]  == "B":
                                canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                              elif getpieceat(Start_x + 5, Start_y) == "None":
                                 canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                                 if getpieceat(Start_x + 6, Start_y)[-1]  == "B":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                 elif getpieceat(Start_x + 6, Start_y) == "None":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x + 7, Start_y)[-1]  == "B":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x + 7, Start_y) == "None":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                      if getpieceat(Start_x + 8, Start_y)[-1]  == "B":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
                                      elif getpieceat(Start_x + 8, Start_y) == "None":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
                if getpieceat(Start_x, Start_y + 1)[-1] == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
                elif getpieceat(Start_x, Start_y + 1) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
                   if getpieceat(Start_x, Start_y + 2)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                   elif getpieceat(Start_x, Start_y + 2) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                      if getpieceat(Start_x, Start_y + 3)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                      elif getpieceat(Start_x, Start_y + 3) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                         if getpieceat(Start_x, Start_y + 4)[-1]  == "B":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                         elif getpieceat(Start_x, Start_y + 4) == "None":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                             if getpieceat(Start_x, Start_y + 5)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                             elif getpieceat(Start_x, Start_y + 5) == "None":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                                if getpieceat(Start_x, Start_y + 6)[-1]  == "B":
                                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                elif getpieceat(Start_x, Start_y + 6) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                  if getpieceat(Start_x, Start_y + 7)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                  elif getpieceat(Start_x, Start_y + 7) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                     if getpieceat(Start_x, Start_y + 8)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
                                     elif getpieceat(Start_x, Start_y + 8) == "None":
                                       canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
                if getpieceat(Start_x, Start_y - 1)[-1]  == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
                elif getpieceat(Start_x, Start_y - 1) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
                   if getpieceat(Start_x, Start_y - 2)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                   elif getpieceat(Start_x, Start_y - 2) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                      if getpieceat(Start_x, Start_y - 3)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                      elif getpieceat(Start_x, Start_y - 3) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                         if getpieceat(Start_x, Start_y - 4)[-1]  == "B":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                         elif getpieceat(Start_x, Start_y - 4) == "None":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                            if getpieceat(Start_x, Start_y - 5)[-1]  == "B":
                              canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                            elif getpieceat(Start_x, Start_y - 5) == "None":
                               canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                               if getpieceat(Start_x, Start_y - 6)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                               elif getpieceat(Start_x, Start_y - 6) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                                  if getpieceat(Start_x, Start_y - 7)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + -6))
                                  elif getpieceat(Start_x, Start_y - 7) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + -7))
                                     if getpieceat(Start_x, Start_y - 8)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
                                     elif getpieceat(Start_x, Start_y - 8) == "None":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
                if getpieceat(Start_x - 1,Start_y)[-1] == "B":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
                elif getpieceat(Start_x - 1,Start_y) == "None":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
                   if getpieceat(Start_x - 2,Start_y)[-1] == "B":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                   elif getpieceat(Start_x - 2,Start_y) == "None":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                      if getpieceat(Start_x - 3,Start_y)[-1] == "B":
                        canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                      elif getpieceat(Start_x - 3,Start_y) == "None":
                         canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                         if getpieceat(Start_x - 4,Start_y)[-1] == "B":
                           canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                         elif getpieceat(Start_x - 4,Start_y) == "None":
                            canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                            if getpieceat(Start_x - 5,Start_y)[-1] == "B":
                               canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                            elif getpieceat(Start_x - 5,Start_y) == "None":
                                canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                                if getpieceat(Start_x - 6,Start_y)[-1] == "B":
                                   canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                elif getpieceat(Start_x - 6,Start_y) == "None":
                                    canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x - 7,Start_y)[-1] == "B":
                                      canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x - 7,Start_y) == "None":
                                       canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                       if getpieceat(Start_x - 8,Start_y)[-1] == "B":
                                         canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
                                       elif getpieceat(Start_x - 8,Start_y) == "None":
                                          canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
    elif SelectedPiece == "KnightW":
       if getpieceat(Start_x - 1,Start_y + 2) == "None" or getpieceat(Start_x + 1,Start_y + 2)[-1] == "B":
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 2))
       if getpieceat(Start_x - 1,Start_y - 2) == "None" or getpieceat(Start_x - 1,Start_y - 2)[-1] == "B":
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 2))
       if getpieceat(Start_x - 1,Start_y + 2) == "None" or getpieceat(Start_x - 1,Start_y + 2)[-1] == "B":
          canmove.append(str(Start_x + -1) + "," + str(Start_y + 2))
       if getpieceat(Start_x - 1,Start_y - 2) == "None" or getpieceat(Start_x + 1,Start_y - 2)[-1] == "B":
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 2))
       if getpieceat(Start_x + 2,Start_y - 1) == "None" or getpieceat(Start_x + 2,Start_y - 1)[-1] == "B":
          canmove.append(str(Start_x + 2) + "," + str(Start_y - 1))
       if getpieceat(Start_x - 2,Start_y - 1) == "None" or getpieceat(Start_x - 2,Start_y - 1)[-1] == "B":
          canmove.append(str(Start_x - 2) + "," + str(Start_y - 1))
       if getpieceat(Start_x + 2,Start_y + 1) == "None" or getpieceat(Start_x + 2,Start_y + 1)[-1] == "B":
          canmove.append(str(Start_x + 2) + "," + str(Start_y + 1))
       if getpieceat(Start_x - 2,Start_y + 1) == "None" or getpieceat(Start_x - 2,Start_y + 1)[-1] == "B":
          canmove.append(str(Start_x - 2) + "," + str(Start_y + 1))         
    elif SelectedPiece == "BishopW":
       if getpieceat(Start_x - 1, Start_y - 1)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
       elif getpieceat(Start_x - 1, Start_y - 1) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x - 2, Start_y - 2)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x - 2, Start_y - 2) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x - 3, Start_y - 3)[-1]  == "B":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x - 3, Start_y - 3) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x - 4, Start_y - 4)[-1]  == "B":
                    canmove.append(str(Start_x + -4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x - 4, Start_y - 4) == "None":
                  canmove.append(str(Start_x + -4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x - 5, Start_y - 5)[-1]  == "B":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x - 5, Start_y - 5) == "None":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x - 6, Start_y - 6)[-1]  == "B":
                     canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y - 6) == "None":
                      canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x - 7, Start_y - 7)[-1]  == "B":
                        canmove.append(str(Start_x + -7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x - 7, Start_y - 7) == "None":
                          canmove.append(str(Start_x + -7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x - 8, Start_y - 8)[-1]  == "B":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x - 8, Start_y - 8) == "None":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
       if getpieceat(Start_x + 1, Start_y + 1)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
       elif getpieceat(Start_x + 1, Start_y + 1) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x + 2, Start_y + 2)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x + 2, Start_y + 2) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x + 3, Start_y + 3)[-1]  == "B":
                canmove.append(str(Start_x +  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x + 3, Start_y + 3) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x + 4, Start_y + 4)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x + 4, Start_y + 4) == "None":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x + 5, Start_y + 5)[-1]  == "B":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x + 5, Start_y + 5) == "None":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x + 6, Start_y + 6)[-1]  == "B":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x + 6, Start_y + 6) == "None":
                       canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x + 7, Start_y + 7)[-1]  == "B":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x + 7, Start_y + 7) == "None":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x + 8, Start_y + 8)[-1]  == "B":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x + 8, Start_y + 8) == "None":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
       if getpieceat(Start_x + 1, Start_y - 1)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
       elif getpieceat(Start_x + 1, Start_y - 1) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x + 2, Start_y - 2)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x + 2, Start_y - 2) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x + 3, Start_y - 3)[-1]  == "B":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x + 3, Start_y - 3) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x + 4, Start_y - 4)[-1]  == "B":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x + 4, Start_y - 4) == "None":
                  canmove.append(str(Start_x + 4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x + 5, Start_y - 5)[-1]  == "B":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x + 5, Start_y - 5) == "None":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x + 6, Start_y - 6)[-1]  == "B":
                     canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y + 6) == "None":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x + 7, Start_y - 7)[-1]  == "B":
                        canmove.append(str(Start_x + 7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x + 7, Start_y - 7) == "None":
                          canmove.append(str(Start_x + 7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x + 8, Start_y - 8)[-1]  == "B":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x + 8, Start_y - 8) == "None":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
       if getpieceat(Start_x - 1, Start_y + 1)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
       elif getpieceat(Start_x - 1, Start_y + 1) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x - 2, Start_y + 2)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x - 2, Start_y + 2) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x - 3, Start_y + 3)[-1]  == "B":
                canmove.append(str(Start_x -  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x - 3, Start_y + 3) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x - 4, Start_y + 4)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x - 4, Start_y + 4) == "None":
                    canmove.append(str(Start_x - 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x - 5, Start_y + 5)[-1]  == "B":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x - 5, Start_y + 5) == "None":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x - 6, Start_y + 6)[-1]  == "B":
                      canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x - 6, Start_y + 6) == "None":
                       canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x - 7, Start_y + 7)[-1]  == "B":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x - 7, Start_y + 7) == "None":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x - 8, Start_y + 8)[-1]  == "B":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x - 8, Start_y + 8) == "None":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
    elif SelectedPiece == "QueenW": 
         if getpieceat(Start_x - 1, Start_y - 1)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
         elif getpieceat(Start_x - 1, Start_y - 1) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x - 2, Start_y - 2)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x - 2, Start_y - 2) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x - 3, Start_y - 3)[-1]  == "B":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x - 3, Start_y - 3) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x - 4, Start_y - 4)[-1]  == "B":
                    canmove.append(str(Start_x + -4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x - 4, Start_y - 4) == "None":
                  canmove.append(str(Start_x + -4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x - 5, Start_y - 5)[-1]  == "B":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x - 5, Start_y - 5) == "None":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x - 6, Start_y - 6)[-1]  == "B":
                     canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y - 6) == "None":
                      canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x - 7, Start_y - 7)[-1]  == "B":
                        canmove.append(str(Start_x + -7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x - 7, Start_y - 7) == "None":
                          canmove.append(str(Start_x + -7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x - 8, Start_y - 8)[-1]  == "B":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x - 8, Start_y - 8) == "None":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
         if getpieceat(Start_x + 1, Start_y + 1)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
         elif getpieceat(Start_x + 1, Start_y + 1) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x + 2, Start_y + 2)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x + 2, Start_y + 2) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x + 3, Start_y + 3)[-1]  == "B":
                canmove.append(str(Start_x +  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x + 3, Start_y + 3) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x + 4, Start_y + 4)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x + 4, Start_y + 4) == "None":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x + 5, Start_y + 5)[-1]  == "B":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x + 5, Start_y + 5) == "None":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x + 6, Start_y + 6)[-1]  == "B":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x + 6, Start_y + 6) == "None":
                       canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x + 7, Start_y + 7)[-1]  == "B":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x + 7, Start_y + 7) == "None":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x + 8, Start_y + 8)[-1]  == "B":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x + 8, Start_y + 8) == "None":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
         if getpieceat(Start_x + 1, Start_y - 1)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
         elif getpieceat(Start_x + 1, Start_y - 1) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x + 2, Start_y - 2)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x + 2, Start_y - 2) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x + 3, Start_y - 3)[-1]  == "B":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x + 3, Start_y - 3) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x + 4, Start_y - 4)[-1]  == "B":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x + 4, Start_y - 4) == "None":
                  canmove.append(str(Start_x + 4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x + 5, Start_y - 5)[-1]  == "B":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x + 5, Start_y - 5) == "None":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x + 6, Start_y - 6)[-1]  == "B":
                     canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y + 6) == "None":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x + 7, Start_y - 7)[-1]  == "B":
                        canmove.append(str(Start_x + 7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x + 7, Start_y - 7) == "None":
                          canmove.append(str(Start_x + 7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x + 8, Start_y - 8)[-1]  == "B":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x + 8, Start_y - 8) == "None":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
         if getpieceat(Start_x - 1, Start_y + 1)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
         elif getpieceat(Start_x - 1, Start_y + 1) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x - 2, Start_y + 2)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x - 2, Start_y + 2) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x - 3, Start_y + 3)[-1]  == "B":
                canmove.append(str(Start_x -  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x - 3, Start_y + 3) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x - 4, Start_y + 4)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x - 4, Start_y + 4) == "None":
                    canmove.append(str(Start_x - 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x - 5, Start_y + 5)[-1]  == "B":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x - 5, Start_y + 5) == "None":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x - 6, Start_y + 6)[-1]  == "B":
                      canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x - 6, Start_y + 6) == "None":
                       canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x - 7, Start_y + 7)[-1]  == "B":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x - 7, Start_y + 7) == "None":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x - 8, Start_y + 8)[-1]  == "B":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x - 8, Start_y + 8) == "None":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
         if getpieceat(Start_x + 1, Start_y)[-1]  == "B":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
         elif getpieceat(Start_x + 1, Start_y) == "None":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
                    if getpieceat(Start_x + 2, Start_y)[-1]  == "B":
                          canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                    elif getpieceat(Start_x + 2, Start_y) == "None":
                        canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                        if getpieceat(Start_x + 3, Start_y)[-1]  == "B":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                        elif getpieceat(Start_x + 3, Start_y) == "None":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                           if getpieceat(Start_x + 4, Start_y)[-1]  == "B":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                           elif getpieceat(Start_x + 4, Start_y) == "None":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                              if getpieceat(Start_x + 5, Start_y)[-1]  == "B":
                                canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                              elif getpieceat(Start_x + 5, Start_y) == "None":
                                 canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                                 if getpieceat(Start_x + 6, Start_y)[-1]  == "B":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                 elif getpieceat(Start_x + 6, Start_y) == "None":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x + 7, Start_y)[-1]  == "B":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x + 7, Start_y) == "None":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                      if getpieceat(Start_x + 8, Start_y)[-1]  == "B":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
                                      elif getpieceat(Start_x + 8, Start_y) == "None":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
         if getpieceat(Start_x, Start_y + 1)[-1] == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
         elif getpieceat(Start_x, Start_y + 1) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
                   if getpieceat(Start_x, Start_y + 2)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                   elif getpieceat(Start_x, Start_y + 2) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                      if getpieceat(Start_x, Start_y + 3)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                      elif getpieceat(Start_x, Start_y + 3) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                         if getpieceat(Start_x, Start_y + 4)[-1]  == "B":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                         elif getpieceat(Start_x, Start_y + 4) == "None":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                             if getpieceat(Start_x, Start_y + 5)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                             elif getpieceat(Start_x, Start_y + 5) == "None":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                                if getpieceat(Start_x, Start_y + 6)[-1]  == "B":
                                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                elif getpieceat(Start_x, Start_y + 6) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                  if getpieceat(Start_x, Start_y + 7)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                  elif getpieceat(Start_x, Start_y + 7) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                     if getpieceat(Start_x, Start_y + 8)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
                                     elif getpieceat(Start_x, Start_y + 8) == "None":
                                       canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
         if getpieceat(Start_x, Start_y - 1)[-1]  == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
         elif getpieceat(Start_x, Start_y - 1) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
                   if getpieceat(Start_x, Start_y - 2)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                   elif getpieceat(Start_x, Start_y - 2) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                      if getpieceat(Start_x, Start_y - 3)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                      elif getpieceat(Start_x, Start_y - 3) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                         if getpieceat(Start_x, Start_y - 4)[-1]  == "B":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                         elif getpieceat(Start_x, Start_y - 4) == "None":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                            if getpieceat(Start_x, Start_y - 5)[-1]  == "B":
                              canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                            elif getpieceat(Start_x, Start_y - 5) == "None":
                               canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                               if getpieceat(Start_x, Start_y - 6)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                               elif getpieceat(Start_x, Start_y - 6) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                                  if getpieceat(Start_x, Start_y - 7)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + -6))
                                  elif getpieceat(Start_x, Start_y - 7) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + -7))
                                     if getpieceat(Start_x, Start_y - 8)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
                                     elif getpieceat(Start_x, Start_y - 8) == "None":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
         if getpieceat(Start_x - 1,Start_y)[-1] == "B":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
         elif getpieceat(Start_x - 1,Start_y) == "None":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
                   if getpieceat(Start_x - 2,Start_y)[-1] == "B":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                   elif getpieceat(Start_x - 2,Start_y) == "None":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                      if getpieceat(Start_x - 3,Start_y)[-1] == "B":
                        canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                      elif getpieceat(Start_x - 3,Start_y) == "None":
                         canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                         if getpieceat(Start_x - 4,Start_y)[-1] == "B":
                           canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                         elif getpieceat(Start_x - 4,Start_y) == "None":
                            canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                            if getpieceat(Start_x - 5,Start_y)[-1] == "B":
                               canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                            elif getpieceat(Start_x - 5,Start_y) == "None":
                                canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                                if getpieceat(Start_x - 6,Start_y)[-1] == "B":
                                   canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                elif getpieceat(Start_x - 6,Start_y) == "None":
                                    canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x - 7,Start_y)[-1] == "B":
                                      canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x - 7,Start_y) == "None":
                                       canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                       if getpieceat(Start_x - 8,Start_y)[-1] == "B":
                                         canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
                                       elif getpieceat(Start_x - 8,Start_y) == "None":
                                          canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
    return canmove


def convertmove(Start_x,Start_y,New_x,New_Y):
   return str(coords[Start_x - 1]) + str(Start_y + 1) + str(coords[New_x - 1]) + str(New_Y + 1)
def allmoveperpiece(canmove,start_x,start_y):
   allmoves = []
   for i in canmove:
      allmoves.append(convertmove(start_x,start_y,int(str(i).split(",")[0]) - 1,int(str(i).split(",")[1])))
   return allmoves
def introanimation(player1,player2): 
    for time in range(10): 
        screen.blit(vsgui,(0,0 + time)) 
pygame.init() 
myfont = pygame.font.SysFont("rockwell", 25) 
gametype = "Intro" 
while running: #While window open 
    intrologo = intrologo.convert_alpha() 
    x = (pygame.mouse.get_pos()[0] / 75) - 2 #Get mouse x be
    y = (pygame.mouse.get_pos()[1] / 75) - 1 #Get mouse y
    piece_x = round(x) #Round mouse x
    piece_y = round(y) #Round mouse y
    
    if gametype == "InGame":
       mixer.music.set_volume(0.5)
       screen.blit(boardimg,(0,7))

       pygame.display.set_caption("Chess.py - Playing a Match")
       if inrange(piece_x,piece_y):
          loadpiece(piece_x - 1,piece_y,"CanMove",False) #Show that green thing       
          loadpiece(x - 1,y,SelectedPiece,True)  #Show selected piece
          showgreenthing = True
       else:
           showgreenthing = False
       loadpieces() #Load pieces from board grid
       showcanmove(canmove)
       screen.blit(menugui,(0,0))
       label = myfont.render(player1, 1, (255,255,0))
       screen.blit(label, (35, 100))
       label = myfont.render(player2, 1, (255,255,0))
       screen.blit(label, (900, 100))
       loadpiece(-2,1,lastselectpiece,False)
    elif gametype == "Menu":
        screen.blit(boardimg,(0,0))
        screen.blit(title,(200,100))
        pygame.display.set_caption("Chess.py")
        if x > 3 and x < 7.6 and y > 4.6 and y < 6.3:
          screen.blit(buttonselect,(270,415))
        else:
            screen.blit(button,(270,415))
    elif gametype == "Intro":
        introtimer -= 1
        if introtimer == 300:
            mixer.music.play(0,0,150)
        if introtimer == 0:
            gametype = "Menu"
        if introtimer > 0 and introtimer < 300:
            screen.blit(intrologo,(0,0))
        else:
            screen.fill(black)
        pygame.display.set_caption("Chess.py")
    events = pygame.event.get() #Get events
    for event in events:  #For every event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #If event was mouse clicked
            if gametype == "Menu": 
             if x > 3 and x < 7.6 and y > 4.6 and y < 6.3 and event.button == 1:
                 gametype = "InGame"
                 screen.blit(menugui,(0,0))
                 introanimation(player1,player2)
            else:
                if showgreenthing:
                   canmovepiece(piece_x,piece_y,canmove)
                   if event.button == 3:
                      if getpieceat(piece_x,piece_y)[-1] == "W":
                         
                         Start_x = piece_x
                         Start_y = piece_y
                         SelectedPiece = getpieceat(Start_x,Start_y) #Choose what piece to move
                         lastselectpiece = SelectedPiece       
                         canmove = [] #Clear canmove
                         handlemovement(Start_x,Start_y,SelectedPiece,board)
                         showcanmove(personalcanmove)
                   elif event.button == 1:
                       if canmovepiece(piece_x,piece_y,canmove):
                         board[(8 * (Start_y)) + (Start_x - 1)] = "None"
                         board[(8 * (piece_y)) + (piece_x - 1)] = SelectedPiece
                         SelectedPiece = "None"
                         canmove = []
                       print(convertmove(Start_x,Start_y,piece_x,piece_y))
            
    
    pygame.display.flip() #Refresh The Screen DO THIS AFTER LOADING PIECES
    pygame.display.set_icon(programIcon)