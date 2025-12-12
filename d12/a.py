import sys
from copy import deepcopy
import time
filename = sys.argv[1]
#def print_grid(s):
#    for r in s:
#        for c in r:
#            print(c, end="")
#        print("")

def rotate(m):
    return list(zip(*m[::-1]))

def flip(grid):
    # horizontal flip
    return [list(reversed(row)) for row in grid]

from copy import deepcopy

fit_memo = {}
count_memo = {}
poss = [0]
rotations = {}
from copy import deepcopy

count_memo = {}
def tupled(grid):
    return tuple(map(tuple, grid))

def fit(grid, tile):
    # returns all grids where tile is positioned
    key = (tupled(grid), tupled(rotations[tupled(tile)][0]))
    if key in fit_memo:
        return fit_memo[key]
 
    M = len(grid)
    N = len(grid[0])
    starts = [(i,j) for i in range(M) for j in range(N)]
    ans = [] 
    for rot in rotations[tupled(tile)]:
        for i, j in starts:
            ng = None
            valid = True
            for ii in range(len(rot)):
                if not valid:
                    break
                for jj in range(len(rot[0])):
                    if not ng: ng = deepcopy(grid)
                    if i+ii not in range(M) or j+jj not in range(N):
                        valid = False
                        break
                    if rot[ii][jj] == ".":
                        pass
                    elif rot[ii][jj] == "#" and ng[i+ii][j+jj] == ".":
                        ng[i+ii][j+jj] = "#"
                    elif rot[ii][jj] == "#" and ng[i+ii][j+jj] == "#":
                        valid = False
                        break
            if valid:
                ans.append(ng) 
    fit_memo[key] = ans
    return ans

def search(grid, N, tiles):
    #print(N)
    #print(grid, N, tiles)
    if poss[0] != 0:
        return
    if sum(N) == 0: 
        #print_grid(grid)
        poss[0] += 1
    # I still have tiles to place
    for i, (n,tile) in enumerate(zip(N, tiles)):
        if n == 0: continue 
        # get all possibile fits
        N[i] -= 1
        poss_fits = fit(grid, tile)
        for pf in poss_fits:
            if pf:
                search(pf, N, tiles)
        N[i] += 1

with open(filename) as f:
    data = f.read().split("\n\n")
    grids = data[-1].splitlines()
    tiles = data[:-1]
    tiles = [[list(y) for y in x.splitlines()[1:]] for x in tiles]
    N = [[int(y) for y in x.split(" ")[1:]] for x in grids] 
    shapes = [[int(y) for y in x.split(" ")[0][:-1].split("x")] for x in grids]
    for tile in tiles:
        r1 = tile
        r2 = rotate(r1)
        r3 = rotate(r2)
        r4 = rotate(r3)
        rotations[tupled(tile)] = [r1,r2,r3,r4]
            
    for shape, n in zip(shapes, N):
        r,c = shape
        grid = [["." for _ in range(r)] for _ in range(c)]
        poss[0] = 0
        search(grid, n, tiles)
        print(poss)