import sys
filename = sys.argv[1]
with open(filename) as f:
    grid = f.read().splitlines()
    M = len(grid)
    N = len(grid[0])
    splits = set()
    tot = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 'S':
                start = (i,j)
            elif grid[i][j] == '^':
                splits.add((i,j))
    i,j = start
    beams = [(i,j)]
    while True:
        new_beams = set()
        B = len(beams)
        for idx in range(B):
            i,j = beams[idx]
            beams[idx] = (i+1,j)
        ended = False
        for r,c in beams:
            if r not in range(M):
                print(len(beams))
                ended = True
                break
            elif (r,c) in splits:
                tot += 1
                if c+1 in range(N):
                    new_beams.add((r,c+1))
                if c-1 in range(N):
                    new_beams.add((r,c-1)) 
            else:
                new_beams.add((r,c))
        if ended:
            break
        beams = list(new_beams)
        print(tot)
            
    
    

