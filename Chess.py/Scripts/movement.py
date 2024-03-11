

def getpieceat(PieceX,PieceY, board):
    pieceindex = (int(8 * PieceY) + (int(PieceX) - 1))
    if pieceindex > -1 and pieceindex < 64:
       return str(board[int(pieceindex)])
    else:
        return "None"



def handlemovement(Start_x,Start_y,SelectedPiece,board): #This is the definition of spaghetti code. Make no attempt to read it, it is the rules for the movement of pieces 
    canmove = []
    if SelectedPiece == "PawnW":
            if Start_y == 6 and board[8 * (Start_y - 2) + (Start_x - 1)] == "None":
                canmove.append(str(Start_x) + "," + str(Start_y - 2))
            if board[8 * (Start_y - 1) + (Start_x - 1)] == "None":
                canmove.append(str(Start_x) + "," + str(Start_y - 1))
            if board[8 * (Start_y - 1) + (Start_x - 2)][-1] == "B":
              canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
            if board[8 * (Start_y - 1) + (Start_x)][-1] == "B":
              canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
    elif SelectedPiece == "PawnB":
            if Start_y == 2 and board[8 * (Start_y + 2) + (Start_x - 1)] == "None":
                canmove.append(str(Start_x) + "," + str(Start_y + 2))
            if board[8 * (Start_y + 1) + (Start_x - 1)] == "None":
                canmove.append(str(Start_x) + "," + str(Start_y + 1))
            if board[8 * (Start_y + 1) + (Start_x - 2)][-1] == "B":
              canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
            if board[8 * (Start_y + 1) + (Start_x)][-1] == "B":
              canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
    elif SelectedPiece == "KingW":
          if getpieceat(Start_x + 1,Start_y,board) == "None" or getpieceat(Start_x + 1,Start_y,board)[-1] == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y))
          if getpieceat(Start_x - 1,Start_y,board) == "None" or getpieceat(Start_x - 1,Start_y,board)[-1] == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y))
          if getpieceat(Start_x + 1,Start_y,board) == "None" or getpieceat(Start_x + 1,Start_y,board)[-1] == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x - 1,Start_y + 1,board) == "None" or getpieceat(Start_x - 1,Start_y + 1,board)[-1] == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x + 1,Start_y - 1,board) == "None" or getpieceat(Start_x + 1,Start_y - 1,board)[-1] == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y -1))
          if getpieceat(Start_x - 1,Start_y - 1,board) == "None" or getpieceat(Start_x - 1,Start_y - 1,board)[-1] == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x,Start_y + 1,board) == "None" or getpieceat(Start_x,Start_y + 1,board)[-1] == "B":
           canmove.append(str(Start_x) + "," + str(Start_y + 1))
          if getpieceat(Start_x,Start_y - 1,board) == "None" or getpieceat(Start_x,Start_y - 1,board)[-1] == "B":
           canmove.append(str(Start_x) + "," + str(Start_y - 1))
    elif SelectedPiece == "RookW":
                if getpieceat(Start_x + 1, Start_y,board)[-1]  == "B":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
                elif getpieceat(Start_x + 1, Start_y,board) == "None":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
                    if getpieceat(Start_x + 2, Start_y,board)[-1]  == "B":
                          canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                    elif getpieceat(Start_x + 2, Start_y,board) == "None":
                        canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                        if getpieceat(Start_x + 3, Start_y,board)[-1]  == "B":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                        elif getpieceat(Start_x + 3, Start_y,board) == "None":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                           if getpieceat(Start_x + 4, Start_y,board)[-1]  == "B":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                           elif getpieceat(Start_x + 4, Start_y,board) == "None":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                              if getpieceat(Start_x + 5, Start_y,board)[-1]  == "B":
                                canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                              elif getpieceat(Start_x + 5, Start_y,board) == "None":
                                 canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                                 if getpieceat(Start_x + 6, Start_y,board)[-1]  == "B":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                 elif getpieceat(Start_x + 6, Start_y,board) == "None":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x + 7, Start_y,board)[-1]  == "B":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x + 7, Start_y,board) == "None":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                      if getpieceat(Start_x + 8, Start_y,board)[-1]  == "B":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
                                      elif getpieceat(Start_x + 8, Start_y,board) == "None":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
                if getpieceat(Start_x, Start_y + 1,board)[-1] == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
                elif getpieceat(Start_x, Start_y + 1,board) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
                   if getpieceat(Start_x, Start_y + 2,board)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                   elif getpieceat(Start_x, Start_y + 2,board) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                      if getpieceat(Start_x, Start_y + 3,board)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                      elif getpieceat(Start_x, Start_y + 3,board) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                         if getpieceat(Start_x, Start_y + 4,board)[-1]  == "B":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                         elif getpieceat(Start_x, Start_y + 4,board) == "None":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                             if getpieceat(Start_x, Start_y + 5,board)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                             elif getpieceat(Start_x, Start_y + 5,board) == "None":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                                if getpieceat(Start_x, Start_y + 6,board)[-1]  == "B":
                                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                elif getpieceat(Start_x, Start_y + 6,board) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                  if getpieceat(Start_x, Start_y + 7,board)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                  elif getpieceat(Start_x, Start_y + 7,board) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                     if getpieceat(Start_x, Start_y + 8,board)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
                                     elif getpieceat(Start_x, Start_y + 8,board) == "None":
                                       canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
                if getpieceat(Start_x, Start_y - 1,board)[-1]  == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
                elif getpieceat(Start_x, Start_y - 1,board) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
                   if getpieceat(Start_x, Start_y - 2,board)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                   elif getpieceat(Start_x, Start_y - 2,board) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                      if getpieceat(Start_x, Start_y - 3,board)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                      elif getpieceat(Start_x, Start_y - 3,board) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                         if getpieceat(Start_x, Start_y - 4,board)[-1]  == "B":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                         elif getpieceat(Start_x, Start_y - 4,board) == "None":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                            if getpieceat(Start_x, Start_y - 5,board)[-1]  == "B":
                              canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                            elif getpieceat(Start_x, Start_y - 5,board) == "None":
                               canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                               if getpieceat(Start_x, Start_y - 6,board)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                               elif getpieceat(Start_x, Start_y - 6,board) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                                  if getpieceat(Start_x, Start_y - 7,board)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + -6))
                                  elif getpieceat(Start_x, Start_y - 7,board) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + -7))
                                     if getpieceat(Start_x, Start_y - 8,board)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
                                     elif getpieceat(Start_x, Start_y - 8,board) == "None":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
                if getpieceat(Start_x - 1,Start_y,board)[-1] == "B":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
                elif getpieceat(Start_x - 1,Start_y,board) == "None":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
                   if getpieceat(Start_x - 2,Start_y,board)[-1] == "B":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                   elif getpieceat(Start_x - 2,Start_y,board) == "None":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                      if getpieceat(Start_x - 3,Start_y,board)[-1] == "B":
                        canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                      elif getpieceat(Start_x - 3,Start_y,board) == "None":
                         canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                         if getpieceat(Start_x - 4,Start_y,board)[-1] == "B":
                           canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                         elif getpieceat(Start_x - 4,Start_y,board) == "None":
                            canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                            if getpieceat(Start_x - 5,Start_y,board)[-1] == "B":
                               canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                            elif getpieceat(Start_x - 5,Start_y,board) == "None":
                                canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                                if getpieceat(Start_x - 6,Start_y,board)[-1] == "B":
                                   canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                elif getpieceat(Start_x - 6,Start_y,board) == "None":
                                    canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x - 7,Start_y,board)[-1] == "B":
                                      canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x - 7,Start_y,board) == "None":
                                       canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                       if getpieceat(Start_x - 8,Start_y,board)[-1] == "B":
                                         canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
                                       elif getpieceat(Start_x - 8,Start_y,board) == "None":
                                          canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
    elif SelectedPiece == "KnightW":
       if getpieceat(Start_x + 1,Start_y + 2,board) == "None" or getpieceat(Start_x + 1,Start_y + 2,board)[-1] == "B":
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 2))
       if getpieceat(Start_x - 1,Start_y - 2,board) == "None" or getpieceat(Start_x - 1,Start_y - 2,board)[-1] == "B":
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 2))
       if getpieceat(Start_x - 1,Start_y + 2,board) == "None" or getpieceat(Start_x - 1,Start_y + 2,board)[-1] == "B":
          canmove.append(str(Start_x + -1) + "," + str(Start_y + 2))
       if getpieceat(Start_x + 1,Start_y - 2,board) == "None" or getpieceat(Start_x + 1,Start_y - 2,board)[-1] == "B":
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 2))
       if getpieceat(Start_x + 2,Start_y - 1,board) == "None" or getpieceat(Start_x + 2,Start_y - 1,board)[-1] == "B":
          canmove.append(str(Start_x + 2) + "," + str(Start_y - 1))
       if getpieceat(Start_x - 2,Start_y - 1,board) == "None" or getpieceat(Start_x - 2,Start_y - 1,board)[-1] == "B":
          canmove.append(str(Start_x - 2) + "," + str(Start_y - 1))
       if getpieceat(Start_x + 2,Start_y + 1,board) == "None" or getpieceat(Start_x + 2,Start_y + 1,board)[-1] == "B":
          canmove.append(str(Start_x + 2) + "," + str(Start_y + 1))
       if getpieceat(Start_x - 2,Start_y + 1,board) == "None" or getpieceat(Start_x - 2,Start_y + 1,board)[-1] == "B":
          canmove.append(str(Start_x - 2) + "," + str(Start_y + 1))         
    elif SelectedPiece == "BishopW":
       if getpieceat(Start_x - 1, Start_y - 1,board)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
       elif getpieceat(Start_x - 1, Start_y - 1,board) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x - 2, Start_y - 2,board)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x - 2, Start_y - 2,board) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x - 3, Start_y - 3,board)[-1]  == "B":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x - 3, Start_y - 3,board) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x - 4, Start_y - 4,board)[-1]  == "B":
                    canmove.append(str(Start_x + -4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x - 4, Start_y - 4,board) == "None":
                  canmove.append(str(Start_x + -4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x - 5, Start_y - 5,board)[-1]  == "B":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x - 5, Start_y - 5,board) == "None":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x - 6, Start_y - 6,board)[-1]  == "B":
                     canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y - 6,board) == "None":
                      canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x - 7, Start_y - 7,board)[-1]  == "B":
                        canmove.append(str(Start_x + -7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x - 7, Start_y - 7,board) == "None":
                          canmove.append(str(Start_x + -7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x - 8, Start_y - 8,board)[-1]  == "B":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x - 8, Start_y - 8,board) == "None":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
       if getpieceat(Start_x + 1, Start_y + 1,board)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
       elif getpieceat(Start_x + 1, Start_y + 1,board) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x + 2, Start_y + 2,board)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x + 2, Start_y + 2,board) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x + 3, Start_y + 3,board)[-1]  == "B":
                canmove.append(str(Start_x +  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x + 3, Start_y + 3,board) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x + 4, Start_y + 4,board)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x + 4, Start_y + 4,board) == "None":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x + 5, Start_y + 5,board)[-1]  == "B":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x + 5, Start_y + 5,board) == "None":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x + 6, Start_y + 6,board)[-1]  == "B":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x + 6, Start_y + 6,board) == "None":
                       canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x + 7, Start_y + 7,board)[-1]  == "B":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x + 7, Start_y + 7,board) == "None":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x + 8, Start_y + 8,board)[-1]  == "B":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x + 8, Start_y + 8,board) == "None":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
       if getpieceat(Start_x + 1, Start_y - 1,board)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
       elif getpieceat(Start_x + 1, Start_y - 1,board) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x + 2, Start_y - 2,board)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x + 2, Start_y - 2,board) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x + 3, Start_y - 3,board)[-1]  == "B":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x + 3, Start_y - 3,board) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x + 4, Start_y - 4,board)[-1]  == "B":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x + 4, Start_y - 4,board) == "None":
                  canmove.append(str(Start_x + 4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x + 5, Start_y - 5,board)[-1]  == "B":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x + 5, Start_y - 5,board) == "None":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x + 6, Start_y - 6,board)[-1]  == "B":
                     canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y + 6,board) == "None":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x + 7, Start_y - 7,board)[-1]  == "B":
                        canmove.append(str(Start_x + 7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x + 7, Start_y - 7,board) == "None":
                          canmove.append(str(Start_x + 7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x + 8, Start_y - 8,board)[-1]  == "B":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x + 8, Start_y - 8,board) == "None":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
       if getpieceat(Start_x - 1, Start_y + 1,board)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
       elif getpieceat(Start_x - 1, Start_y + 1,board) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x - 2, Start_y + 2,board)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x - 2, Start_y + 2,board) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x - 3, Start_y + 3,board)[-1]  == "B":
                canmove.append(str(Start_x -  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x - 3, Start_y + 3,board) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x - 4, Start_y + 4,board)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x - 4, Start_y + 4,board) == "None":
                    canmove.append(str(Start_x - 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x - 5, Start_y + 5,board)[-1]  == "B":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x - 5, Start_y + 5,board) == "None":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x - 6, Start_y + 6,board)[-1]  == "B":
                      canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x - 6, Start_y + 6,board) == "None":
                       canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x - 7, Start_y + 7,board)[-1]  == "B":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x - 7, Start_y + 7,board) == "None":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x - 8, Start_y + 8,board)[-1]  == "B":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x - 8, Start_y + 8,board) == "None":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
    elif SelectedPiece == "QueenW": 
         if getpieceat(Start_x - 1, Start_y - 1,board)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
         elif getpieceat(Start_x - 1, Start_y - 1,board) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x - 2, Start_y - 2,board)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x - 2, Start_y - 2,board) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x - 3, Start_y - 3,board)[-1]  == "B":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x - 3, Start_y - 3,board) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x - 4, Start_y - 4,board)[-1]  == "B":
                    canmove.append(str(Start_x + -4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x - 4, Start_y - 4,board) == "None":
                  canmove.append(str(Start_x + -4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x - 5, Start_y - 5,board)[-1]  == "B":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x - 5, Start_y - 5,board) == "None":
                   canmove.append(str(Start_x + -5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x - 6, Start_y - 6,board)[-1]  == "B":
                     canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y - 6,board) == "None":
                      canmove.append(str(Start_x + -6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x - 7, Start_y - 7,board)[-1]  == "B":
                        canmove.append(str(Start_x + -7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x - 7, Start_y - 7,board) == "None":
                          canmove.append(str(Start_x + -7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x - 8, Start_y - 8,board)[-1]  == "B":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x - 8, Start_y - 8,board) == "None":
                            canmove.append(str(Start_x + -8) + "," + str(Start_y + -8))
         if getpieceat(Start_x + 1, Start_y + 1,board)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
         elif getpieceat(Start_x + 1, Start_y + 1,board) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x + 2, Start_y + 2,board)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x + 2, Start_y + 2,board) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x + 3, Start_y + 3,board)[-1]  == "B":
                canmove.append(str(Start_x +  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x + 3, Start_y + 3,board) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x + 4, Start_y + 4,board)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x + 4, Start_y + 4,board) == "None":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x + 5, Start_y + 5,board)[-1]  == "B":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x + 5, Start_y + 5,board) == "None":
                      canmove.append(str(Start_x + 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x + 6, Start_y + 6,board)[-1]  == "B":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x + 6, Start_y + 6,board) == "None":
                       canmove.append(str(Start_x + 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x + 7, Start_y + 7,board)[-1]  == "B":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x + 7, Start_y + 7,board) == "None":
                         canmove.append(str(Start_x + 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x + 8, Start_y + 8,board)[-1]  == "B":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x + 8, Start_y + 8,board) == "None":
                           canmove.append(str(Start_x + 8) + "," + str(Start_y + 8))
         if getpieceat(Start_x + 1, Start_y - 1,board)[-1]  == "B":
           canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
         elif getpieceat(Start_x + 1, Start_y - 1,board) == "None":
          canmove.append(str(Start_x + 1) + "," + str(Start_y - 1))
          if getpieceat(Start_x + 2, Start_y - 2,board)[-1]  == "B":
            canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
          elif getpieceat(Start_x + 2, Start_y - 2,board) == "None":
             canmove.append(str(Start_x + 2) + "," + str(Start_y - 2))
             if getpieceat(Start_x + 3, Start_y - 3,board)[-1]  == "B":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
             elif getpieceat(Start_x + 3, Start_y - 3,board) == "None":
                canmove.append(str(Start_x + 3) + "," + str(Start_y - 3))
                if getpieceat(Start_x + 4, Start_y - 4,board)[-1]  == "B":
                    canmove.append(str(Start_x + 4) + "," + str(Start_y - 4))
                elif getpieceat(Start_x + 4, Start_y - 4,board) == "None":
                  canmove.append(str(Start_x + 4) + "," + str(Start_y + -4))
                  if getpieceat(Start_x + 5, Start_y - 5,board)[-1]  == "B":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                  elif getpieceat(Start_x + 5, Start_y - 5,board) == "None":
                   canmove.append(str(Start_x + 5) + "," + str(Start_y + -5))
                   if getpieceat(Start_x + 6, Start_y - 6,board)[-1]  == "B":
                     canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                   elif getpieceat(Start_x, Start_y + 6,board) == "None":
                      canmove.append(str(Start_x + 6) + "," + str(Start_y + -6))
                      if getpieceat(Start_x + 7, Start_y - 7,board)[-1]  == "B":
                        canmove.append(str(Start_x + 7) + "," + str(Start_y + -6))
                      elif getpieceat(Start_x + 7, Start_y - 7,board) == "None":
                          canmove.append(str(Start_x + 7) + "," + str(Start_y + -7))
                          if getpieceat(Start_x + 8, Start_y - 8,board)[-1]  == "B":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
                          elif getpieceat(Start_x + 8, Start_y - 8,board) == "None":
                            canmove.append(str(Start_x + 8) + "," + str(Start_y + -8))
         if getpieceat(Start_x - 1, Start_y + 1,board)[-1]  == "B":
           canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
         elif getpieceat(Start_x - 1, Start_y + 1,board) == "None":
          canmove.append(str(Start_x - 1) + "," + str(Start_y + 1))
          if getpieceat(Start_x - 2, Start_y + 2,board)[-1]  == "B":
            canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
          elif getpieceat(Start_x - 2, Start_y + 2,board) == "None":
             canmove.append(str(Start_x - 2) + "," + str(Start_y + 2))
             if getpieceat(Start_x - 3, Start_y + 3,board)[-1]  == "B":
                canmove.append(str(Start_x -  3) + "," + str(Start_y + 3))
             elif getpieceat(Start_x - 3, Start_y + 3,board) == "None":
                canmove.append(str(Start_x - 3) + "," + str(Start_y + 3))
                if getpieceat(Start_x - 4, Start_y + 4,board)[-1]  == "B":
                   canmove.append(str(Start_x + 4) + "," + str(Start_y + 4))
                elif getpieceat(Start_x - 4, Start_y + 4,board) == "None":
                    canmove.append(str(Start_x - 4) + "," + str(Start_y + 4))
                    if getpieceat(Start_x - 5, Start_y + 5,board)[-1]  == "B":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    elif getpieceat(Start_x - 5, Start_y + 5,board) == "None":
                      canmove.append(str(Start_x - 5) + "," + str(Start_y + 5))
                    if getpieceat(Start_x - 6, Start_y + 6,board)[-1]  == "B":
                      canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                    elif getpieceat(Start_x - 6, Start_y + 6,board) == "None":
                       canmove.append(str(Start_x - 6) + "," + str(Start_y + 6))
                       if getpieceat(Start_x - 7, Start_y + 7,board)[-1]  == "B":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 6))
                       elif getpieceat(Start_x - 7, Start_y + 7,board) == "None":
                         canmove.append(str(Start_x - 7) + "," + str(Start_y + 7))
                         if getpieceat(Start_x - 8, Start_y + 8,board)[-1]  == "B":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
                         elif getpieceat(Start_x - 8, Start_y + 8,board) == "None":
                           canmove.append(str(Start_x - 8) + "," + str(Start_y + 8))
         if getpieceat(Start_x + 1, Start_y,board)[-1]  == "B":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
         elif getpieceat(Start_x + 1, Start_y,board) == "None":
                    canmove.append(str(Start_x + 1) + "," + str(Start_y + 0))
                    if getpieceat(Start_x + 2, Start_y,board)[-1]  == "B":
                          canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                    elif getpieceat(Start_x + 2, Start_y,board) == "None":
                        canmove.append(str(Start_x + 2) + "," + str(Start_y + 0))
                        if getpieceat(Start_x + 3, Start_y,board)[-1]  == "B":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                        elif getpieceat(Start_x + 3, Start_y,board) == "None":
                           canmove.append(str(Start_x + 3) + "," + str(Start_y + 0))
                           if getpieceat(Start_x + 4, Start_y,board)[-1]  == "B":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                           elif getpieceat(Start_x + 4, Start_y,board) == "None":
                              canmove.append(str(Start_x + 4) + "," + str(Start_y + 0))
                              if getpieceat(Start_x + 5, Start_y,board)[-1]  == "B":
                                canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                              elif getpieceat(Start_x + 5, Start_y,board) == "None":
                                 canmove.append(str(Start_x + 5) + "," + str(Start_y + 0))
                                 if getpieceat(Start_x + 6, Start_y,board)[-1]  == "B":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                 elif getpieceat(Start_x + 6, Start_y,board) == "None":
                                    canmove.append(str(Start_x + 6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x + 7, Start_y,board)[-1]  == "B":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x + 7, Start_y,board) == "None":
                                      canmove.append(str(Start_x + 7) + "," + str(Start_y + 0))
                                      if getpieceat(Start_x + 8, Start_y,board)[-1]  == "B":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
                                      elif getpieceat(Start_x + 8, Start_y,board ) == "None":
                                          canmove.append(str(Start_x + 8) + "," + str(Start_y + 0))
         if getpieceat(Start_x, Start_y + 1,board)[-1] == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
         elif getpieceat(Start_x, Start_y + 1,board) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 1))
                   if getpieceat(Start_x, Start_y + 2,board)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                   elif getpieceat(Start_x, Start_y + 2,board) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y + 2))
                      if getpieceat(Start_x, Start_y + 3,board)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                      elif getpieceat(Start_x, Start_y + 3,board) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y + 3))
                         if getpieceat(Start_x, Start_y + 4,board)[-1]  == "B":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                         elif getpieceat(Start_x, Start_y + 4,board) == "None":
                             canmove.append(str(Start_x + 0) + "," + str(Start_y + 4))
                             if getpieceat(Start_x, Start_y + 5,board)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                             elif getpieceat(Start_x, Start_y + 5,board) == "None":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y + 5))
                                if getpieceat(Start_x, Start_y + 6,board)[-1]  == "B":
                                   canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                elif getpieceat(Start_x, Start_y + 6,board) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y + 6))
                                  if getpieceat(Start_x, Start_y + 7,board)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                  elif getpieceat(Start_x, Start_y + 7,board) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + 7))
                                     if getpieceat(Start_x, Start_y + 8,board)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
                                     elif getpieceat(Start_x, Start_y + 8,board) == "None":
                                       canmove.append(str(Start_x + 0) + "," + str(Start_y + 8))
         if getpieceat(Start_x, Start_y - 1,board)[-1]  == "B":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
         elif getpieceat(Start_x, Start_y - 1,board) == "None":
                   canmove.append(str(Start_x + 0) + "," + str(Start_y - 1))
                   if getpieceat(Start_x, Start_y - 2,board)[-1]  == "B":
                     canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                   elif getpieceat(Start_x, Start_y - 2,board) == "None":
                      canmove.append(str(Start_x + 0) + "," + str(Start_y - 2))
                      if getpieceat(Start_x, Start_y - 3,board)[-1]  == "B":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                      elif getpieceat(Start_x, Start_y - 3,board) == "None":
                         canmove.append(str(Start_x + 0) + "," + str(Start_y - 3))
                         if getpieceat(Start_x, Start_y - 4,board)[-1]  == "B":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                         elif getpieceat(Start_x, Start_y - 4,board) == "None":
                            canmove.append(str(Start_x + 0) + "," + str(Start_y - 4))
                            if getpieceat(Start_x, Start_y - 5,board)[-1]  == "B":
                              canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                            elif getpieceat(Start_x, Start_y - 5,board) == "None":
                               canmove.append(str(Start_x + 0) + "," + str(Start_y - 5))
                               if getpieceat(Start_x, Start_y - 6,board)[-1]  == "B":
                                canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                               elif getpieceat(Start_x, Start_y - 6,board) == "None":
                                  canmove.append(str(Start_x + 0) + "," + str(Start_y - 6))
                                  if getpieceat(Start_x, Start_y - 7,board)[-1]  == "B":
                                    canmove.append(str(Start_x + 0) + "," + str(Start_y + -6))
                                  elif getpieceat(Start_x, Start_y - 7,board) == "None":
                                     canmove.append(str(Start_x + 0) + "," + str(Start_y + -7))
                                     if getpieceat(Start_x, Start_y - 8,board)[-1]  == "B":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
                                     elif getpieceat(Start_x, Start_y - 8,board) == "None":
                                        canmove.append(str(Start_x + 0) + "," + str(Start_y + -8))
         if getpieceat(Start_x - 1,Start_y,board)[-1] == "B":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
         elif getpieceat(Start_x - 1,Start_y,board) == "None":
                   canmove.append(str(Start_x + -1) + "," + str(Start_y + 0))
                   if getpieceat(Start_x - 2,Start_y,board)[-1] == "B":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                   elif getpieceat(Start_x - 2,Start_y,board) == "None":
                      canmove.append(str(Start_x + -2) + "," + str(Start_y + 0))
                      if getpieceat(Start_x - 3,Start_y,board)[-1] == "B":
                        canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                      elif getpieceat(Start_x - 3,Start_y,board) == "None":
                         canmove.append(str(Start_x + -3) + "," + str(Start_y + 0))
                         if getpieceat(Start_x - 4,Start_y,board)[-1] == "B":
                           canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                         elif getpieceat(Start_x - 4,Start_y,board) == "None":
                            canmove.append(str(Start_x + -4) + "," + str(Start_y + 0))
                            if getpieceat(Start_x - 5,Start_y,board)[-1] == "B":
                               canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                            elif getpieceat(Start_x - 5,Start_y,board) == "None":
                                canmove.append(str(Start_x + -5) + "," + str(Start_y + 0))
                                if getpieceat(Start_x - 6,Start_y,board)[-1] == "B":
                                   canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                elif getpieceat(Start_x - 6,Start_y,board) == "None":
                                    canmove.append(str(Start_x + -6) + "," + str(Start_y + 0))
                                    if getpieceat(Start_x - 7,Start_y,board)[-1] == "B":
                                      canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                    elif getpieceat(Start_x - 7,Start_y,board) == "None":
                                       canmove.append(str(Start_x + -7) + "," + str(Start_y + 0))
                                       if getpieceat(Start_x - 8,Start_y,board)[-1] == "B":
                                         canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
                                       elif getpieceat(Start_x - 8,Start_y,board) == "None":
                                          canmove.append(str(Start_x + -8) + "," + str(Start_y + 0))
    return(canmove)