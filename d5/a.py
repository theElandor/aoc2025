import sys
filename = sys.argv[1]
with open(filename) as f:
    ranges, nums = f.read().split("\n\n")
    ranges = [x.split("-") for x in ranges.splitlines()]
    nums = [int(x) for x in nums.splitlines()]
    total = 0
    print(ranges, nums) 
    for n in nums:
        for s,e in ranges:
            if int(s) <= n <= int(e):
                print(n)
                total += 1
                break
    print(total)
    
