import sys
directions = [(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1),(-1,-1),(1,1)]
filename = sys.argv[1]
def print_grid(grid, valid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in valid:
                print("x", end="")
            else:
                print(grid[i][j], end="")
        print("")
                
with open(filename) as f:
    grid = f.read().splitlines()
    print(grid)
    M = len(grid)
    N = len(grid[0])
    total = 0
    valid = set()
    for i in range(M):
        for j in range(N):
            counter = 0
            if grid[i][j] != "@":
                continue
            for dx, dy in directions:
                x = i+dx
                y = j+dy
                if x in range(M) and y in range(N):
                    print(x,y)
                    if grid[x][y] == "@":
                        counter += 1
            if counter < 4:
                valid.add((i,j))
                total += 1
    print(total)
    #print_grid(grid, valid)
            
