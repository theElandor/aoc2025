import sys
filename = sys.argv[1]
from functools import cache

splits = set()



with open(filename) as f:
    grid = f.read().splitlines()
    M = len(grid)
    N = len(grid[0])
    splits = set()
    tot = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 'S':
                start = (i,j)
            elif grid[i][j] == '^':
                splits.add((i,j))
    @cache 
    def explore(cp):
        r,c = cp
        if r == len(grid):
            return 1
        if c not in range(len(grid[0])):
            return 0
        elif cp in splits:
            return explore((r,c+1)) + explore((r,c-1))
        else:
            return explore((r+1, c))

    print(explore(start))
    
    
            
    
    

