import sys
import time
from copy import deepcopy
import os
directions = [(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1),(-1,-1),(1,1)]
filename = sys.argv[1]
def print_grid(grid, valid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in valid:
                print("x", end="")
            else:
                print(grid[i][j], end="")
        print("")

def get_rem(grid):
    valid = set()
    for i in range(M):
        for j in range(N):
            counter = 0
            if grid[i][j] != "@":
                continue
            for dx, dy in directions:
                x = i+dx
                y = j+dy
                if x in range(M) and y in range(N):
                    if grid[x][y] == "@":
                        counter += 1
            if counter < 4:
                valid.add((i,j))
    return valid

with open(filename) as f:
    grid = [list(x) for x in f.read().splitlines()]
    print(grid)
    M = len(grid)
    N = len(grid[0])
    total = 0 
    while True:
        time.sleep(0.1)
        print_grid(grid, set())
        to_remove = get_rem(grid)
        if len(to_remove) == 0:
            break
        new_grid = deepcopy(grid)
        total += len(to_remove)
        for x,y in to_remove:
            new_grid[x][y] = "."
        grid = new_grid
    print(total)
            


