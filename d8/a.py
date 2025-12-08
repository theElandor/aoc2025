import syfrom collections import defaultdict
import math

def distance(a,b):
    x1,y1,z1 = a
    x2,y2,z2 = b
    return math.sqrt(pow(x1-x2,2) + pow(y1-y2,2) + pow(z1-z2,2))

def find(x,P):
    if P[x] != x:
        P[x] = find(P[x], P)
    return P[x]

def union(x,y,P):
    px = find(x,P)
    py = find(y,P)
    if px == py: return
    P[py] = px

filename = sys.argv[1]
limit = int(sys.argv[2])
with open(filename) as f:
    B  = [tuple(map(int, x.split(","))) for x in f.read().splitlines()]
    P = {t:t for t in B}
    distances = []
    for i in range(len(B)):
        for j in range(i+1, len(B)):
            a = B[i]
            b = B[j]
            distances.append((distance(a,b), a,b))
    distances = sorted(distances, key=lambda x:x[0])
    print(distances)
    for d,a,b in distances[:limit]:
        if find(a,P) != find(b,P): 
            union(a,b,P)
    t = 1
    for i,val in enumerate(sorted(list(R.values()), reverse=True)[:3]):
        print(i, val)
        t *= val
    print(t)     
