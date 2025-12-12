import sys
from copy import deepcopy
import time
filename = sys.argv[1]

def get_area(tile):
    total = 0
    for r in tile:
        for c in r:
            if c == "#":
                total += 1 
    return total

with open(filename) as f:
    data = f.read().split("\n\n")
    grids = data[-1].splitlines()
    tiles = data[:-1]
    tiles = [[list(y) for y in x.splitlines()[1:]] for x in tiles]
    N = [[int(y) for y in x.split(" ")[1:]] for x in grids] 
    shapes = [[int(y) for y in x.split(" ")[0][:-1].split("x")] for x in grids]
    ans = 0
    for shape, n in zip(shapes, N):
        tot_area = 0
        for i,tile in enumerate(tiles):
            tot_area += get_area(tile)*n[i]
        if tot_area*1.2 <= shape[0]*shape[1]:
            ans += 1
    print(ans)