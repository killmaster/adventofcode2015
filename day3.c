#include <stdio.h>
#include <stdlib.h>

int main()
{
  static int const WORLD_SIZE = 190;
  int world[WORLD_SIZE][WORLD_SIZE];
  int x = WORLD_SIZE/2, y = WORLD_SIZE/2,
      w = WORLD_SIZE/2, z = WORLD_SIZE/2;
  int count = 0;
  char character;
  int i,j;

  FILE *fp = fopen("day3input.txt","r");

  world[x][y] = 1;
  while((character = fgetc(fp)) != EOF)
  {
    switch (character) {
      case '>':
      if((count % 2) != 0)
        x += 1;
      else
        w += 1;
      break;
      case '<':
      if((count % 2) != 0)
        x -= 1;
      else
        w -= 1;
      break;
      case '^':
      if((count % 2) != 0)
        y += 1;
      else
        z += 1;
      break;
      case 'v':
      if((count % 2) != 0)
        y -= 1;
      else
        z -= 1;
      break;
    }
    world[x][y] = 12345;
    world[w][z] = 12345;
    count++;
  }

  count = 0;

  for(i = 0; i <= WORLD_SIZE; i++)
  {
    for(j = 0; j <= WORLD_SIZE; j++)
    {
      if(world[i][j] == 12345)
        count += 1;
    }
  }
  printf("%d\n",count);
}
