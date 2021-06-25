import random

def checkRange(grid, p, q):
    try:
        grid[q][p + 1] += 100
    except Exception:
        pass

def setBoard(gridNum, mineNum):
    grid = [[-1] * gridNum for i in range(gridNum)]
    count = 0
    while(count <= mineNum):
        p = random.randint(0, gridNum - 1)
        q = random.randint(0, gridNum - 1)
        if(grid[q][p] > -2):

            grid[q][p] += -10000

            checkRange(grid, p-1, q-1)
            checkRange(grid, p-1, q)
            checkRange(grid, p-1, q+1)
            checkRange(grid, p, q-1)
            checkRange(grid, p, q+1)
            checkRange(grid, p+1, q)
            checkRange(grid, p+1, q+1)
            checkRange(grid, p+1, q)

            count += 1

            print(grid)
# def printBoard(gridnum):

if __name__ == "__main__":
    setBoard(9, 9)
