import sys
from functools import cache
filename = sys.argv[1]

def find_largest(s, k= 12):
    n = len(s)
    drops = n - k
    result = [] 
    for digit in s:
        while result and digit > result[-1] and drops > 0:
            result.pop()
            drops -= 1 
        result.append(digit)
    return int("".join(result[:k]))
        
with open(filename) as f:
    total = 0
    lines = f.read().splitlines()
    for line in lines:
        total += find_larges(line)
    print(total)
