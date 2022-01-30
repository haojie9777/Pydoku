"""
Simple sudoku solver using recursion and backtracking
"""

bd = [[0,3,0,1,0,0,0,0,0],
      [2,0,0,0,3,6,0,8,0],
      [0,0,0,4,0,0,0,0,6],
      [0,9,0,0,6,2,0,0,7],
      [0,0,7,0,0,0,0,1,0],
      [0,0,0,0,0,4,0,0,0],
      [8,0,0,0,0,0,5,0,0],
      [0,0,0,3,0,0,0,0,0],
      [0,2,0,0,9,7,0,0,1]]

def printBoard(bd):
    for i,row in enumerate(bd):
        if i%3 == 0 and i!= 0:
            print("___ ___ ___ ___ ___ ___")
        for j,col in enumerate(row):
            if j%3==0 and j!= 0:
                print(" | ", end ="")
            if j != 8:  
                print(str(col) + " ", end= "")
            else:
                print(col)
    return


def getEmpty(bd):
    for row in range(len(bd)):
        for col in range(len(bd[0])):
            if bd[row][col] == 0:
                return (row,col)
    return -1

    
def valid(bd,row,col,num):
    #check row
    for column in bd[row]:
        if column == num:
            return False
    #check col
    for i in range(9):
        if bd[i][col] == num:
            return False
    #check square containing the grid that we are currently checking
    boxRow = row //3
    boxCol = col//3
    for i in range(boxRow*3,boxRow*3 + 3):
        for j in range(boxCol*3, boxCol*3 +3):
            if bd[i][j] == num:
                return False
    return True

def solve(bd):
    empty = getEmpty(bd)
    #board is alrdy fully solved
    if empty == -1:
        return True
    row,col = empty
    for i in range(1,10):
        if valid(bd,row,col,i):
            bd[row][col] = i
            #recursively solve for next empty grid once sucessfully placed this grid
            if solve(bd):
                return True
            #backtrack if not a valid solution
            bd[row][col] = 0
    #can't find any solution after searching through all search spaces
    return False


printBoard(bd)
if solve(bd):
    print("Solution:")
    printBoard(bd)
else:
    print("no solution")

