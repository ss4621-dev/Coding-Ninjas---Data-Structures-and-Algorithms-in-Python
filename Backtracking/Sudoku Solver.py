
    
def solveSudoku(board):
    row = [dict() for i in range(9)]
    col = [dict() for i in range(9)]
    subGrid = [[dict() for j in range(3)] for i in range(3)]
    
    for r in range(9):
        for c in range(9):
            if(board[r][c] == 0):
                continue
            
            if(board[r][c] in subGrid[r//3][c//3] or board[r][c] in col[c] or board[r][c] in row[r]):
                return False
            
            subGrid[r//3][c//3][board[r][c]] = True
            row[r][board[r][c]] = True
            col[c][board[r][c]] = True
            
    return True

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')
