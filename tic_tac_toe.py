import numpy as np
import random
from time import sleep

# empty board
def empty_board():
    board=np.array([
                   [0,0,0],
                   [0,0,0],
                   [0,0,0]
                   ])
    return(board)

# check empty places
def empty_space(board):
    l=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                l.append((i,j))
    return(l)

# Select random space for player
def random_space(board,player):
    select=empty_space(board)
    current_loc=random.choice(select)
    board[current_loc]= player
    return(board)

# winner or tie
def row_winner(board,player):
    for i in range(len(board)):
        win= True
        for j in range(len(board)):
            if board[i,j]!= player:
                win= False
                continue
        if win==True:
            return(win)
    return(win)
def col_winner(board,player):
    for i in range(len(board)):
        win=True
        for j in range(len(board)):
            if board[j,i]!= player:
                win=False
                continue
        if win==True:
            return(win)
    return(win)
def dia_winner(board, player):
    win = True
    # Check primary diagonal
    for i in range(len(board)):
        if board[i, i] != player:
            win = False
            break
    if win:
        return True
    
    win = True
    # Check secondary diagonal
    for i in range(len(board)):
        if board[i, len(board) - 1 - i] != player:
            win = False
            break
    return win
def evaluate_winner(board):
    # winner {0=game not complete , 1= player1 , 2= player2, -1= tie}
    winner=0
    for player in [1,2]:
        if (row_winner(board,player) or col_winner(board,player) or dia_winner(board,player)):
            winner=player
    if np.all(board!=0) and winner==0:
        winner=-1
    return winner


# main function 
def tic_tac_toe():
    board = empty_board()
    winner = 0
    counter = 1
    print(board)
    sleep(4)

    while winner == 0:
        for player in [1, 2]:
            board = random_space(board, player)
            print(f'Board after {counter} move(s):')
            print(board)
            sleep(4)
            counter += 1
            winner = evaluate_winner(board)
            if winner != 0:
                break
        if winner != 0:
            break
    return winner
winner = tic_tac_toe()
if winner == -1:
    print("The game is a tie!")
else:
    print(f"The winner is player {winner}!")


    
