import sys
filename = sys.argv[1]
with open(filename) as f:
    total = 0
    lines =  [[int(x) for x in line] for line in f.read().splitlines()]
    for line in lines:
        print(line)
        first = max(line)
        idx = line.index(first)
        if idx == len(line)-1:
            second = first
            first = max(line[:-1])
            print(int(str(first)+str(second)))
            total += int(str(first)+str(second))
            continue
        second = max(line[idx+1:])
        total += int(str(first)+str(second))
    print(total)
        
        
        