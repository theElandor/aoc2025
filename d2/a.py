import sys
filename = sys.argv[1]

def check(n):
    n = str(n)
    if len(n) % 2 != 0:
        return False
    first, second = n[:len(n)//2], n[len(n)//2:]
    if first == second:
        return True

with open(filename) as f:
    data = f.read()
    ranges = [tuple(map(int, x.split("-"))) for x in data.split(",")]
    counter = 0
    for x,y in ranges:
        for n in range(x,y+1):
            if check(n): counter += n
    print(counter)