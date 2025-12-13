'''
YAFRC (Yet another failed raycasting implementation)
I am so bad at raycasting!
'''

import sys
from itertools import combinations
filename = sys.argv[1]
memo = {}
def raycast(B,v):
    if v in memo: return memo[v]
    if v in B: 
        return True
    x,y = v
    times = 0
    for o in range(100000):
        if (x+o, y) in B:
            if (x+o+1, y) not in B:
               times += 1 
    memo[v] = ((times%2) != 0)
    return (times % 2) != 0
        
with open(filename) as f:
    V = [tuple(map(int, x.split(","))) for x in f.read().splitlines()]
    B = set()
    for v1,v2 in zip(V, V[1:]+[V[0]]):
        x1, y1 = v1
        x2, y2 = v2
        if x1 == x2:
            maxim = max(y1,y2)
            minim = min(y1,y2)
            for i in range(minim, maxim+1):
                B.add((x1,i))
        elif y1 == y2:
            maxim = max(x1,x2)
            minim = min(x1,x2)
            for i in range(minim, maxim+1):
                B.add((i,y1))
    C = list(combinations(V,2))
    m = float("-inf")
    best_pair = None
    for i,(v1,v2) in enumerate(C):
        if i % 1000 == 0:
            print(f"{i}/{len(C)}")
        x1,y1 = v1
        x2, y2 = v2
        p1 = (x1,y2)
        p2 = (x2,y1)
        if not all([raycast(B, point) for point in [p1,p2]]):
            continue
        area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
        if area > m:
            best_pair = v1,v2
            m = area
            print(m)
    print(best_pair)
    print(m)
