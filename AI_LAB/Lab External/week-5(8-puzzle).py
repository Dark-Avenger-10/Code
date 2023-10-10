answer=[1,2,3,
        4,5,6,
        7,8,9]
        
def print_board(board):
    for i in range(9):
        if i>0 and i%3==0:
            print()
        print(board[i],end=" ")

def count(board):
    c=0
    for i in range(9):
        if board[i]!=0 and board[i]!=answer[i]:
            c+=1
    return c

def move(pos,arr,curr_board):
    opt=9999
    borad=curr_board.copy()
    opt_board=curr_board.copy()
    
    for i in arr:
        temp=curr_board.copy()
        #Swapping
        temp[pos],temp[i]=temp[i],temp[pos]
        
        c=count(temp)

        if c<opt:
            opt=c
            opt_board=[i for i in temp]
    
    #print(opt_board,opt)
    return opt_board,opt

board=[1,2,3,
       0,5,6,
       4,7,8]

h=count(board)
step=1

print("Current State of the Board : ")
print_board(board)
print("\nMisplaced Tiles : ",h)

while h>0:
    pos=board.index(0)
    
    if pos==0:
        arr=[1,3]
        board,h=move(pos,arr,board)
    elif pos==1:
        arr=[0,2,4]
        board,h=move(pos,arr,board)
    elif pos==2:
        arr=[1,5]
        board,h=move(pos,arr,board)
    elif pos==3:
        arr=[0,4,6]
        board,h=move(pos,arr,board)
    elif pos==4:
        arr=[1,3,5,7]
        board,h=move(pos,arr,board)
    elif pos==5:
        arr=[2,4,6]
        board,h=move(pos,arr,board)
    elif pos==6:
        arr=[3,7]
        board,h=move(pos,arr,board)
    elif pos==7:
        arr=[4,6,8]
        board,h=move(pos,arr,board)
    elif pos==8:
        arr=[5,7]
        board,h=move(pos,arr,board)
    
    print("Step #",step,sep="")
    print_board(board)
    print("\nMisplaced Tiles : ",h)
    step+=1

    
        