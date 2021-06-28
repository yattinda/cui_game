import random
import numpy as np

#-1で飛ぶことを防ぐ
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

def printBoard(gridNum, grid, status):
    print("\n")
    print(" ", end = "  ")
    for i in range(1, gridNum + 1):
        print(i, end = "   ")

    print("\n")

    for j in range(gridNum):
        print(j + 1 ,end  = " ")
        for k in range(gridNum):
            if(grid[j][k] < -100):
                if(status == 666):
                    print(" ☠ ", end = " ")
                elif(status == 999):
                    print(" ■ ", end = " ")
            elif(int(str(grid[j][k])[-1]) == 0):
                print(" ■ ", end = " ")
            else:
                if(10 > grid[j][k] and grid[j][k] > 0):
                    print(" ・", end = " ")
                elif(int(str(grid[j][k])[-3]) > 0):
                    print(" " + str(grid[j][k])[-3] + " ", end  = " ")
        print("\n")
    print("\n")

def checkClear(grid, gridNum, mineNum):
    count = 0
    for i in range(gridNum):
        for k in range(gridNum):
            if(grid[i][k] == -666):
                count += 1

    if(count == mineNum):
        return 500
    else:
        return -500

def open(p, q, gridNum, grid):
    if(p < 0 or p > gridNum - 1 or q < 0 or q > gridNum - 1):
        return None
    elif(int(str(grid[p][q])[-1]) != 0):
        return None
    else:
        grid[p][q] += 1
        open(p-1, q-1, gridNum, grid)
        open(p-1, q, gridNum, grid)
        open(p-1, q+1, gridNum, grid)
        open(p, q-1, gridNum, grid)
        open(p, q+1, gridNum, grid)
        open(p+1, q-1, gridNum, grid)
        open(p+1, q, gridNum, grid)
        open(p+1, q+1, gridNum, grid)

def judge(p, q, grid):
    if(grid[p][q] < 0 and int(str(grid[p][q])[-1]) != 0):
        return 666
    return 999

def mainGame():
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("   Hello this is MineSweeper")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    while True:
        level = int(input("Please enter the level at number\n1: EASY\n2: NOMAL\n3: HARD\n"))
        if(level == 1):
            gridNum = 9
            mineNum = 10
            break
        elif(level == 2):
            gridNum = 16
            mineNum = 40
            break
        elif(level == 3):
            gridNum = 20
            mineNum = 100
            break
        else:
            print("Please enter 1 or 2 or 3")

    setBoard(gridNum, mineNum)
    printBoard(gridNum, grid, 999)

    while True:
        a, b = (int(x) for x in input("Plz enter number! \nFirst, enter the numbers on the side, such as 1 2\n\n" ).split())
        open(a, b, gridNum, grid)
        if(judge(a, b, grid) == 666):
            print("Game over!")
            printBoard(gridNum, grid, 666)
            break
        elif(checkClear(grid, gridNum, mineNum) == 500):
            print("Game clear!")
            printBoard(gridNum, grid, 999)
            break
        else:
            printBoard(gridNum, grid, 999)
            continue


# def test():
#     setBoard(9, 9)
#     printBoard(9, grid)

if __name__ == "__main__":
    mainGame()
