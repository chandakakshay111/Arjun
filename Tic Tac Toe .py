
# Feature required
# 1] printing Board
# 2] Take a player input
# 3] Check win or tie
# 4] Switch player
# 5] Check for win or tie  this will loop continuously
# Board Design


import random


board=["-","-","-",
       "-","-","-",   
       "-","-","-",] 

# Player _COnfiguration
current_player="X"
winner=None
gameRunning=True


def printboard(board):
    print(board[0]+'|'+board[1]+'|'+board[2]+'|')
    print('_____________________________________')
    print(board[3]+'|'+board[4]+'|'+board[5]+'|')
    print('_____________________________________')
    print(board[6]+'|'+board[7]+'|'+board[8]+'|')
    print('_____________________________________')
    

#Taking input to position players
def playerinput(board):
    inp=int(input("Enter Position:"))
    if board[inp-1]=='-':
        board[inp-1]=current_player
    else:
        print("Position is already taken")
        
def check_horizonatal(board):
    global winner
    if board[0]==board[1]==board[2] !='-':
        winner=board[0]
        return True
    if board[3]==board[4]==board[5] !='-':
        winner=board[0]
        return True
    if board[6]==board[7]==board[8] !='-':
        winner=board[0]
        return True
    
    
def check_vertical(board):
    global winner
    if board[0]==board[3]==board[6] !='-':
        winner=board[0]
        return True
    if board[1]==board[4]==board[7] !='-':
        winner=board[0]
        return True
    if board[2]==board[5]==board[8] !='-':
        winner=board[0]
        return True
    
def check_diag(board):
    global winner
    if board[0]==board[4]==board[8] !='-':
        winner=board[0]
        return True
    if board[2]==board[4]==board[6] !='-':
        winner=board[0]
        return True
    
    
    
def winorlose(board):
    global gameRunning
    if check_horizonatal(board):
        printboard(board)
        print(f"Thw winner is {winner}!")
        gameRunning=False
    if check_vertical(board):
        printboard(board)
        print(f"Thw winner is {winner}!")
        gameRunning=False
    if check_diag(board):
        printboard(board)
        print(f"Thw winner is {winner}!")
        gameRunning=False
        
#    Switching the player     
def switch_player():
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"
        
# def computr(board):
#     while current_player == "O":
#         position = random.randint(1, 8)
#         if board[position - 1] == '-':
#             board[position - 1] = current_player
#         else:
#             print("Position is already taken")
            
        
    
    
def tie(board):
    if '-' not in board:
        global gameRunning
        gameRunning=False
        return gameRunning
       
while gameRunning:
    printboard(board)
    playerinput(board)
    winorlose(board)
    tie(board)
    switch_player()
    # computr(board)
    winorlose(board)
    tie(board)
    