import random

def setBoard(gridNum, mineNum):
    grid = [[-1] * gridNum for i in range(gridNum)]
    count = 0
    while(count <= mineNum):
        p = random.randint(0, gridNum - 1)
        q = random.randint(0, gridNum - 1)
        # print(p, q)
        # print(grid[q][p])
        if(grid[q][p] > -2):

            grid[q][p] += -10000

            grid[q][p + 1] += 100
            grid[q][p - 1] += 100
            grid[q + 1][p - 1] += 100
            grid[q + 1][p] += 100
            grid[q + 1][p + 1] += 100
            grid[q - 1][p - 1] += 100
            grid[q - 1][p] += 100
            grid[q - 1][p + 1] += 100

            count += 1

            print(grid)
# def printBoard(gridnum):

if __name__ == "__main__":
    setBoard(9, 9)
