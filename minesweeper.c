#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int difficult (int difficulty){
  int gridNum, mineNum;
  if (difficulty == 99){
    gridNum = 9;
    mineNum = 9;
  } else if (difficulty == 100){
    gridNum = 16;
    mineNum = 40;
  } else {
    gridNum = 3;
    mineNum = 1;
  }
  return gridNum, mineNum;
}

// int **grid = (int**)malloc(gridNum*sizeof(int*));
//
// for(int i = 0; i < gridNum; i++){
//     grid[i]=(int*)malloc(gridNum*sizeof(int));
// }

void setBoard(int gridNum, int mineNum) {
  int **grid = (int**)malloc(gridNum*sizeof(int*));

  for(int i = 0; i < gridNum; i++){
      grid[i]=(int*)malloc(gridNum*sizeof(int));
  }

  for (int x = 0; x <= gridNum; x++){
    for (int y = 0; y <= gridNum; y++){
      grid[y][x] = -1;
    }
  }

  srand((unsigned int)time(NULL));

  for (int j = 1; j <= mineNum; j++){
    int p, q;
    do {
      p = rand() % mineNum + 1;
      q = rand() % mineNum + 1;
    }
    while(grid[q][p] > -2);

      grid[q][p] = -100;

      grid[q][p + 1] += 1;
      grid[q][p - 1] += 1;
      grid[q + 1][p - 1] += 1;
      grid[q + 1][p] += 1;
      grid[q + 1][p + 1] += 1;
      grid[q - 1][p - 1] += 1;
      grid[q - 1][p] += 1;
      grid[q - 1][p + 1] += 1;
  }
}

void printBoard(int gridNum){
  printf("\n  ");
  for(int i = 1; i <= gridNum; i++){
    printf("%i ", gridNum);
  }
  printf("\n");

  for (int y = 1; y <= gridNum; y++){
    printf("%i ", gridNum);
    for (int x = 1; x <= gridNum; x++){
      if (grid[y][x] == -1) {
        printf("■");
      } else if (grid[y][x] == 0){
        printf("・");
      } else if (grid[y][x] < -1){
        printf("＊");
      } else {
        printf("%i", grid[y][x]);
      }
    printf("\n");
    }
  printf("\n");
  }
}

int checkClear(int gridNum, int mineNum){
  int count = 0;
  for (int y = 1; y < gridNum; y++){
    for (int x = 1; x < gridNum; x++){
      if(grid[y][x] > -1){
        count++;
      }
    }
  }
  if (count == gridNum * gridNum - mineNum){
    return 500;
  }
  return -500;
}

void open(int x, int y, int gridNum){
  if(x < 1 || x > gridNum || y < 1 || y > gridNum){
    return ;
  } else if (grid[y][x] != -1){
    return ;
  } else {
    open(x, y - 1);
    open(x - 1, y - 1);
    open(x - 1, y);
    open(x - 1, y + 1);
    open(x, y + 1);
    open(x + 1, y + 1);
    open(x + 1, y);
    open(x + 1, y - 1);
  }
}

int main(){
  printf("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n");
  printf("   Hello this is MineSweeper\n");
  printf("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n");
  for(;;){
    printf("Please enter the level at number\n1: EASY\n2: HIGH\n")
    scanf("%i", l);
    difficult(l);
  }
}
