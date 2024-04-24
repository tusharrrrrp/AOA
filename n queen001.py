global N
N=4
def printingsolution(board):
    for i in range (N):
        for j in range ( N):
             print(board[i][j],end='')
        print()

def is_safe(board,row,col):
    for  j in range (col):
        if board[row][j]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
def SolveNQutil(board,col):
    if col>=N:
        return True
    for i in range(N):
        if is_safe(board,i,col):
            board[i][col]=1
            if SolveNQutil(board,col+1)==True:
                return True
            board[i][col]=0
    return False

def SolveNQ():
    board = [[0, 0, 0, 0, ],
             [0, 0, 0, 0, ],
             [0, 0, 0, 0, ],
             [0, 0, 0, 0, ]
             ]
    if SolveNQutil(board,0)== False:
        print("fo")
        return False

    printingsolution(board)
    return True
SolveNQ()
