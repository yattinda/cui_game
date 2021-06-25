import random
import numpy as np

def checkRange(gridNum,grid, p, q):
    try:
        if(p != -1):
            if(q != -1):
                grid[q][p] += 100
    except Exception:
        pass

def setBoard(gridNum, mineNum):
    grid = np.full((gridNum, gridNum), 0)
    count = 0
    while(count < mineNum):
        p = random.randint(0, gridNum - 1)
        q = random.randint(0, gridNum - 1)
        if(grid[q][p] > -2):
            print(p, q)
            grid[q][p] += -10000

            checkRange(gridNum, grid, p-1, q-1)
            checkRange(gridNum, grid, p-1, q)
            checkRange(gridNum, grid, p-1, q+1)
            checkRange(gridNum, grid, p, q-1)
            checkRange(gridNum, grid, p, q+1)
            checkRange(gridNum, grid, p+1, q-1)
            checkRange(gridNum, grid, p+1, q)
            checkRange(gridNum, grid, p+1, q+1)

            count += 1

            print(grid)
            print("\n\n")
# def printBoard(gridnum):

if __name__ == "__main__":
    setBoard(9, 9)
