import sys
filename = sys.argv[1]


def explore(G, current):
    if current == "out":
        return 1
    else:
        if current in G: 
            tot = 0
            for v in G[current]:
                tot += explore(G,v)
            return tot
    return 0
            
with open(filename) as f:
    data = {x.split(" ")[0][:-1]:x.split(" ")[1:] for x in f.read().splitlines()}
    print(explore(data, "you"))
