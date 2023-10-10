import numpy as np
import random
from time import sleep

def create_board():
    return (np.array([[0,0,0],[0,0,0],[0,0,0]]))

def empty_places(board):
    state=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                state.append((i,j))
    return state

def random_place(board,player):
    places=empty_places(board)
    current_loc=random.choice(places)
    board[current_loc]=player
    return board

def row_win(board,player):
    for i in range(len(board)):
        win=True
        for j in range(len(board)):
            if board[i][j]!=player:
                win=False
                break
        if win:
            return win
    return win

def col_win(board,player):
    for i in range(len(board)):
        win=True
        for j in range(len(board)):
            if board[j][i]!=player:
                win=False
                break
        if win:
            return win
    return win

def diagonal_win(board,player):
    win,y=True,0
    for i in range(len(board)):
        if board[i][i]!=player:
            win=False
    if win:
        return win
    win=True
    for i in range(len(board)):
        y=len(board)-1-i
        if board[i][y]!=player:
            win=False
    return win

def board_state(board):
    winner=0
    for player in [1,2]:
        if row_win(board,player) or col_win(board,player) or diagonal_win(board,player):
            winner=player
    if np.all(board!=0) and winner==0:
        winner=-1
    return winner

def play_game():
    board,winner,counter=create_board(),0,1
    print(board)
    sleep(2)
   
    while winner==0:
        for player in [1,2]:
            board=random_place(board,player)
            print("Board after "+str(counter)+" move")
            print(board)
            sleep(2)
            counter+=1
            winner=board_state(board)
           
            if winner!=0:
                break
    return winner

winner=str(play_game())
if winner==-1:
    print("No winner, It's a Tie ")
else:
    print("Winner is Player",winner)