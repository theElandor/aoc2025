import sys
filename = sys.argv[1]
with open(filename) as f:
    ranges, nums = f.read().split("\n\n")
    ranges = [x.split("-") for x in ranges.splitlines()]
    ranges = [(int(x), int(y)) for x, y in ranges]
    sr = sorted(ranges, key=lambda x:x[0])
    total = 0
    s,e = sr[0]
    for cs, ce in sr:
        if ce <= e:
            continue
        elif cs > e:
            total += (e-s+1)
            s = cs
            e = ce
        else:
            e = ce
    total += (e-s)+1
    print(total)
    
