import sys
from itertools import combinations
filename = sys.argv[1]
with open(filename) as f:
    V = [tuple(map(int, x.split(","))) for x in f.read().splitlines()]
    print(V)
    print(len(V))
    C = list(combinations(V,2))
    areas = []
    m = float("-inf")
    best_pair = None
    for v1,v2 in C:
        x1,y1 = v1
        x2, y2 = v2
        area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
        if area > m:
            best_pair = v1,v2
            m = area
    print(m)
    print(best_pair)
    
