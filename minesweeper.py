import random
import numpy as np

def checkRange(gridNum,grid, p, q):
    try:
        if(p != -1):
            if(q != -1):
                grid[p][q] += 100
    except Exception:
        pass

def setBoard(gridNum, mineNum):
    global grid
    grid = np.full((gridNum, gridNum), 0)
    count = 0
    while(count < mineNum):
        p = random.randint(0, gridNum - 1)
        q = random.randint(0, gridNum - 1)
        if(grid[p][q] > -2):
            grid[p][q] += -10000

            checkRange(gridNum, grid, p-1, q-1)
            checkRange(gridNum, grid, p-1, q)
            checkRange(gridNum, grid, p-1, q+1)
            checkRange(gridNum, grid, p, q-1)
            checkRange(gridNum, grid, p, q+1)
            checkRange(gridNum, grid, p+1, q-1)
            checkRange(gridNum, grid, p+1, q)
            checkRange(gridNum, grid, p+1, q+1)

            count += 1

    # print(grid)

def printBoard(gridnum, grid):
    print(" ", end = "  ")
    for i in range(1, gridnum + 1):
        print(i, end = "   ")

    print("\n")

    for j in range(gridnum):
        print(j + 1 ,end  = " ")
        for k in range(gridnum):
            if(grid[j][k] < -100):
                #最終的に■に
                print(" ★ ", end = " ")
            elif(int(str(grid[j][k])[-1]) == 0):
                print(" ■ ", end = " ")
            else:
                if(10 > grid[j][k] and grid[j][k] > 0):
                    print(" ・ ", end = " ")
                elif(int(str(grid[j][k])[-3]) > 0):
                    print(" " + str(grid[j][k])[-3] + " ", end  = " ")
        print("\n")
    print("\n")

def test():
    setBoard(9, 9)
    printBoard(9, grid)

if __name__ == "__main__":
    test()
