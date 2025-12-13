'''
Here we just check, for every rectangle (start
from the biggest first) that there are no edges
inside it. In that case, the rectangle is partially 
outside, so we don't consider it. If it is valid,
then we can print the area and block the loop.
'''


import sys
filename = sys.argv[1]
def get_size(v1,v2):
    x1,y1 = v1
    x2,y2 = v2
    x = abs(x1 - x2) + 1
    y = abs(y1 - y2) + 1
    return x * y

def get_rect(v1,v2):
    x1,y1 = v1
    x2,y2 = v2
    return (x2,y1), (x1,y2)

def valid(v1,v2,poly):
    # checks each edge
    x1,y1 = v1
    x2,y2 = v2
    #print("RECT")
    #print(v1,v2)
    for p1,p2 in poly:
        p1,p2 = sorted([p1,p2])
        p1x,p1y = p1
        p2x,p2y = p2
        if (p2x > x1 and p1x < x2 and p2y > y1 and p1y < y2):
            return False
    return True
        

with open(filename) as f:
    V = [tuple(map(int, x.split(","))) for x in f.read().splitlines()]
    poly = []
    rects = []
    for v1, v2 in zip(V, V[1:]+[V[0]]):
       poly.append((v1,v2))

    for i in range(len(V)):
        for j in range(i+1, len(V)):
            v1, v2 = V[i], V[j]
            rects.append((get_size(v1,v2), v1,v2))

    sorted_rects = sorted(rects, key = lambda x:x[0], reverse=True)
    for size, v1,v2 in sorted_rects:
        # step 1: get all 4 vertices and take top left and bottom right
        points = sorted([v1,v2, *get_rect(v1,v2)])
        v1,v2 = points[0], points[-1]
        if valid(v1,v2, poly):
            print(size)
            break            
