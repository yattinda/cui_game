#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// int gridNum, mineNum;
// if (difficulty == 99){
//   gridNum = 9 + 2;
//   mineNum = 9;
// } else if (difficulty == 100){
//   gridNum = 16 + 2;
//   mineNum = 40;
// } else {
//   gridNum = 3;
//   mineNum = 1;
// }

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
    while(grid[q][p] != -2);

      grid[q][p] = -2;

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
  for(int i = 1; i <= gridNum - 2; i++){
    printf("%i ", gridNum);
  }
  printf("\n");

  for (int y = 1; y <= gridNum - 2; y++){
    printf("%i ", gridNum);
    for (int x = 1; x <= gridNum - 2; x++){
      if (grid[y][x] == -1) {
        printf("■");
      } else if (grid[y][x] == 0){
        printf("・");
      } else {
        printf("%i", grid[y][x]);
      }
    printf("\n");
    }
  printf("\n");
  }
}
