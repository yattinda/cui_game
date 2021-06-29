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
                if(grid[j][k] and grid[j][k] == 1):
                    print(" ・", end = " ")
                elif(int(str(grid[j][k])[-3]) > 0):
                    print(" " + str(grid[j][k])[-3] + " ", end  = " ")
        print("\n")
    print("\n")
    #debug
    print(grid)

def checkClear(grid, gridNum, mineNum):
    count = 0
    for i in range(gridNum):
        for j in range(gridNum):
            if(int(str(grid[i][j])[-1]) == 1):
                count += 1
    print(count)
    print(gridNum * gridNum - mineNum)
    if(count == gridNum * gridNum - mineNum):
        return 555
    else:
        return -555


def open(p, q, gridNum, grid, gridOpen, count = 0):
    if(p == 999 and q == 999):
        return None
    elif(p < 0 or p > gridNum - 1 or q < 0 or q > gridNum - 1):
        return None
    elif(int(str(grid[p][q])[-1]) != 0):
        return None
    elif(int(str(grid[p][q]/100)[-1]) > 0 or count == gridOpen):
        grid[p][q] += 1
    else:
        grid[p][q] += 1
        count += 1
        open(p-1, q-1, gridNum, grid, gridOpen, count)
        open(p-1, q, gridNum, grid, gridOpen, count)
        open(p-1, q+1, gridNum, grid, gridOpen, count)
        open(p, q-1, gridNum, grid, gridOpen, count)
        open(p, q+1, gridNum, grid, gridOpen, count)
        open(p+1, q-1, gridNum, grid, gridOpen, count)
        open(p+1, q, gridNum, grid, gridOpen, count)
        open(p+1, q+1, gridNum, grid, gridOpen, count)

def judge(p, q, grid):
    if(grid[p][q] < 0 and int(str(grid[p][q])[-1]) != 0):
        return 666
    return 999

def mainGame():
    print("\n")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("   Hello this is MineSweeper")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("\n")
    while True:
        level = int(input("Please enter the level at numbers!\n1: EASY\n2: NOMAL\n3: HARD\n"))
        if(level == 1):
            gridNum = 9
            mineNum = 10
            gridOpen = 2
            break
        elif(level == 2):
            gridNum = 16
            mineNum = 40
            gridOpen = 4
            break
        elif(level == 3):
            gridNum = 20
            mineNum = 100
            gridOpen = 6
            break
        else:
            print("Please enter 1 or 2 or 3")

    setBoard(gridNum, mineNum)
    printBoard(gridNum, grid, 999)
    pinList = []
    while True:
        print("This is your PIN")
        for i in pinList:
            print(i, end = "  ")
        print("\n")
        while True:
            try:
                a, b = (int(x) for x in input("Plz enter number! \nFirst, enter the numbers on the side, such as 1 2\n\nIf u want to use PIN, plz enter 999 999\n\nIf U want to exit, plz enter -666 -666\n").split())
                break
            except:
                print("\n")
                print("$$$$$$$$$$$$$$$$$$$$$$$$")
                print("Plz enter correct number")
                print("$$$$$$$$$$$$$$$$$$$$$$$$")
                print("\n")
                continue
        # PIN mode
        if(a == 999 and b == 999):
            while  True:
                print("\n")
                print("#############################")
                print("          PIN mode           ")
                print("#############################")
                print("\n")
                try:
                    a, b = (int(x) for x in input("Plz enter PIN number! \nFirst, enter the numbers on the side, such as 1 2\n\nIf u NOT want to use PIN, plz enter 999 999\nIf you delete PIN, U enter same PIN\n").split())
                    if(a == 999 and b == 999):
                        printBoard(gridNum, grid, 999)
                        break
                    else:
                        if([a, b] in pinList):
                            pinList.remove([a, b])
                        else:
                            pinList.append([a, b])
                            continue
                except:
                    print("\n")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("Plz enter correct number")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("\n")
                    continue
        #exit
        elif(a == -666 and b == -666):
            exit()

        if(a < 1 or a > 9 or b < 1 or b > 9):
            print("Plz enter correct number")
            continue
        else:
            open(a-1, b-1, gridNum, grid, gridOpen)
            if(judge(a-1, b-1, grid) == 666):
                print("Game over!")
                printBoard(gridNum, grid, 666)
                break
            elif(checkClear(grid, gridNum, mineNum) == 555):
                print("Game clear!")
                printBoard(gridNum, grid, 666)
                break
            else:
                printBoard(gridNum, grid, 999)
                continue


# def test():
#     setBoard(9, 9)
#     printBoard(9, grid)

if __name__ == "__main__":
    mainGame()
