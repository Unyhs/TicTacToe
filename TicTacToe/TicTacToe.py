board={1:' ', 2: ' ',3:' ',
        4:' ', 5: ' ',6:' ',
        7:' ', 8: ' ',9:' '}

player="O"
computer="X"

def printBoard(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-+-+-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-+-+-")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("\n")

def isSpaceFree(position):
    if(board[position]!=' '):
        return False
    else:
        return True

def insertSymbol(symbol,position):
    if(isSpaceFree(position)):
        board[position]=symbol
        printBoard(board)
        if(checkDraw()):
            print("Its a draw!")
            exit()
        elif(checkWin()):
            if(symbol==computer):
                print("The bot wins!")
                exit()
            else:
                print("The player wins!")
                exit()
        return
    else:
        print("This space is already full")
        position=int(input("Please enter a new position from 1 to 9: "))
        insertSymbol(symbol,position)
        return

def checkDraw():
    for key in board.keys():
        if(board[key]==" "):
            return False
    return True

def checkWin():
    if   (board[1]==board[2] and board[1]==board[3] and board[1]!=" "):
        return True
    elif (board[4]==board[5] and board[4]==board[6] and board[4]!=" "):
        return True
    elif (board[7]==board[8] and board[7]==board[9] and board[7]!=" "):
        return True
    elif (board[1]==board[4] and board[1]==board[7] and board[1]!=" "):
        return True
    elif (board[2]==board[5] and board[2]==board[8] and board[2]!=" "):
        return True
    elif (board[3]==board[6] and board[3]==board[9] and board[3]!=" "):
        return True
    elif (board[1]==board[5] and board[1]==board[9] and board[1]!=" "):
        return True
    elif (board[3]==board[5] and board[3]==board[7] and board[3]!=" "):
        return True
    return False

def checkWhichSymbolWon(symbol):
    if   (board[1]==board[2] and board[1]==board[3] and board[1]==symbol):
        return True
    elif (board[4]==board[5] and board[4]==board[6] and board[4]==symbol):
        return True
    elif (board[7]==board[8] and board[7]==board[9] and board[7]==symbol):
        return True
    elif (board[1]==board[4] and board[1]==board[7] and board[1]==symbol):
        return True
    elif (board[2]==board[5] and board[2]==board[8] and board[2]==symbol):
        return True
    elif (board[3]==board[6] and board[3]==board[9] and board[3]==symbol):
        return True
    elif (board[1]==board[5] and board[1]==board[9] and board[1]==symbol):
        return True
    elif (board[3]==board[5] and board[3]==board[7] and board[3]==symbol):
        return True
    return False

def playerMove():
    position=int(input("Hello Player ! Enter your position from 1 to 9. "))
    while(position<1 or position>9):
        print("Not a valid input.")
        position=int(input("Enter your position from 1 to 9. "))

    insertSymbol(player,position)
    return

def computerMove():
    bestScore=-800
    bestMove=0
    for key in board.keys():
        if(board[key]==" "):
            board[key]=computer
            score=minimax(board,False)
            board[key]=" "
            if(score>bestScore):
                bestScore=score
                bestMove=key
    insertSymbol(computer,bestMove)
    return

def minimax(board,isMaximizing):
    if(checkWhichSymbolWon(computer)):
        return 1
    elif (checkWhichSymbolWon(player)):
        return -1
    elif(checkDraw()):
        return 0

    if(isMaximizing):
        bestScore=-800
        for key in board.keys():
            if(board[key]==" "):
                board[key]=computer
                score=minimax(board,False)
                board[key]=" "
                if(score>bestScore):
                    bestScore=score
        return bestScore
    
    else:
        bestScore=800
        for key in board.keys():
            if(board[key]==" "):
                board[key]=player
                score=minimax(board,True)
                board[key]=" "
                if(score<bestScore):
                    bestScore=score
        return bestScore
    
while not checkWin():
    playerMove()
    computerMove()
    
    
        



    








       
    




    
