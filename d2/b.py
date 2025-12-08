import sys
from itertools import batched
from collections import Counter
filename = sys.argv[1]

def check(n):
    n = str(n)
    for l in range(1, len(n)+1):
        if len(n) % l != 0:
            continue
        c = Counter(batched(n, l)) 
        if len(c) == 1 and next(iter(c.values())) != 1:
            return True
    return False

with open(filename) as f:
    data = f.read()
    ranges = [tuple(map(int, x.split("-"))) for x in data.split(",")]
    counter = 0
    for x,y in ranges:
        for n in range(x,y+1):
            if check(n): counter += n
    print(counter)