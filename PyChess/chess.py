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
black = (255, 255, 255)
w = 1000
h = 700
screen = pygame.display.set_mode((w, h))
screen.fill((black))
running = 1
movementx = 0
movementy = 0
SelectedPiece = "None"
piece_x = 0
piece_y = 0
Start_x = 0
Start_y = 0
canmove = []
player1 = "Player"
player2 = "Bot"
showgreenthing = True
lastselectpiece = "None"



mixer.init()
mixer.music.load("Sound/Enough_Plucks.wav")
  
#
mixer.music.set_volume(0.7)
king = [
    "1,1","0,1","-1,1","-1,0","-1,-1","0,-1","1,-1","1,0"
] 

board = [
    "CastleB","KnightB","BishopB","QueenB","KingB","BishopB","KnightB","CastleB",
    "PawnB","PawnB","PawnB","PawnB","PawnB","PawnB","PawnB","PawnB",
    "None","None","None","None","None","None","None","None",
    "None","None","None","None","None","None","None","None",
    "None","None","None","None","None","None","None","None",
    "None","None","None","None","None","None","None","None",
    "PawnW","PawnW","PawnW","PawnW","PawnW","PawnW","PawnW","PawnW",
    "CastleW","KnightW","BishopW","QueenW","KingW","BishopW","KnightW","CastleW"
]
def intro():
    for i in range(1000):
        screen.blit(intrologo,(0,0))
def loadpiece(X,Y,Piece,IsMovingPiece):
    if Piece != "None" and Piece != None: 
        if IsMovingPiece:
            screen.blit(pygame.image.load("Images/Pieces/" + str(Piece) + ".jpeg"),((int(X) * 75)+ 200 + movementx,(int(Y) * 75)+ 60 + movementy)) #Get image file name from Piece, and x/y
        else: 
            screen.blit(pygame.image.load("Images/Pieces/" + str(Piece) + ".jpeg"),((int(X) * 75)+ 200,(int(Y) * 75)+ 60)) #Get image file name from Piece, and x/y
def loadpieces():
    for i in range(len(board)): #For every piece on the board
        if i // 8 == 7 and board[i] == "PawnB":
            board[i] = "QueenB"
        elif i // 8 == 0 and board[i] == "PawnW":
            board[i] = "QueenW"
        loadpiece(i % 8, i // 8, board[i],False) #Find x and y from index, show piece on board
def getpieceat(PieceX,PieceY):
    pieceindex = (int(8 * PieceY) + (int(PieceX) - 1))
    return str(board[int(pieceindex)])
def canmovepiece(piece_x,piece_y,canmove):
    return str(piece_x) + "," + str(piece_y) in canmove
def inrange(piece_x,piece_y):
    if piece_x > 0 and piece_x < 9 and piece_y > -1 and piece_y < 8:
          return True
    else:
          return False
def showcanmove(canmove):
    for i in canmove:
        x = int(str(i).split(",")[0]) - 1
        y = int(str(i).split(",")[1])
        loadpiece(x,y,"CanMove",False)
def handlemovement(Start_x,Start_y,SelectedPiece):
    if SelectedPiece == "PawnW":
            if Start_y == 6:
                canmove.append(str(Start_x) + "," + str(Start_y - 2))
            canmove.append(str(Start_x) + "," + str(Start_y - 1))
    elif SelectedPiece == "KingW":
          canmove.append(str(Start_x + 1) + "," + str(Start_y))
          canmove.append(str(Start_x - 1) + "," + str(Start_y))
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
          canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          canmove.append(str(Start_x) + "," + str(Start_y - 1))
          canmove.append(str(Start_x) + "," + str(Start_y + 1))
    elif SelectedPiece == "CastleW":
        canmove.append(str(Start_x + 1) + "," + str(Start_y))
        canmove.append(str(Start_x + 2) + "," + str(Start_y))
        canmove.append(str(Start_x + 3) + "," + str(Start_y))
        canmove.append(str(Start_x + 4) + "," + str(Start_y))
        canmove.append(str(Start_x + 5) + "," + str(Start_y))
        canmove.append(str(Start_x + 6) + "," + str(Start_y))
        canmove.append(str(Start_x + 7) + "," + str(Start_y))
        canmove.append(str(Start_x - 1) + "," + str(Start_y))
        canmove.append(str(Start_x - 2) + "," + str(Start_y))
        canmove.append(str(Start_x - 3) + "," + str(Start_y))
        canmove.append(str(Start_x - 4) + "," + str(Start_y))
        canmove.append(str(Start_x - 5) + "," + str(Start_y))
        canmove.append(str(Start_x - 6) + "," + str(Start_y))
        canmove.append(str(Start_x - 7) + "," + str(Start_y))
        canmove.append(str(Start_x) + "," + str(Start_y + 1))
        canmove.append(str(Start_x) + "," + str(Start_y + 2))
        canmove.append(str(Start_x) + "," + str(Start_y + 3))
        canmove.append(str(Start_x) + "," + str(Start_y + 4))
        canmove.append(str(Start_x) + "," + str(Start_y + 5))
        canmove.append(str(Start_x) + "," + str(Start_y + 6))
        canmove.append(str(Start_x) + "," + str(Start_y + 7))
        canmove.append(str(Start_x) + "," + str(Start_y - 1))
        canmove.append(str(Start_x) + "," + str(Start_y - 2))
        canmove.append(str(Start_x) + "," + str(Start_y - 3))
        canmove.append(str(Start_x) + "," + str(Start_y - 4))
        canmove.append(str(Start_x) + "," + str(Start_y - 5))
        canmove.append(str(Start_x) + "," + str(Start_y - 6))
        canmove.append(str(Start_x) + "," + str(Start_y - 7))
        for i in canmove:
          x = int(str(i).split(",")[0])
          y = int(str(i).split(",")[1])
          if not inrange(x,y):
              del canmove[canmove.index(i)]
        
        showcanmove(canmove)
def introanimation(player1,player2):
    for time in range(10):
        screen.blit(vsgui,(0,0 + time))
mixer.music.play(-1,0,150)
pygame.init()
myfont = pygame.font.SysFont("rockwell", 25)
intro()
gametype = "Menu"
while running: #While window open
    showcanmove(canmove)
    x = (pygame.mouse.get_pos()[0] / 75) - 2 #Get mouse x
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
       showcanmove(canmove)
       loadpieces() #Load pieces from board grid
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
                         canmove = [] #Clear canmove
                         Start_x = piece_x
                         Start_y = piece_y
                         SelectedPiece = getpieceat(Start_x,Start_y) #Choose what piece to move
                         lastselectpiece = SelectedPiece       
                         handlemovement(Start_x,Start_y,SelectedPiece)
                   elif event.button == 1:
                       if canmovepiece(piece_x,piece_y,canmove):
                         board[(8 * (Start_y)) + (Start_x - 1)] = "None"
                         board[(8 * (piece_y)) + (piece_x - 1)] = SelectedPiece
                         SelectedPiece = "None"
                         canmove = []
            
    
    pygame.display.flip() #Refresh The Screen DO THIS AFTER LOADING PIECES
    pygame.display.set_icon(programIcon)