import sys
filename = sys.argv[1]

#paths = []
#def explore(G, current, path):
#    if current == "out":
#        paths.append(path)
#        return
#    if current in G:
#        for v in G[current]:
#            explore(G, v, path + f" {v}")
#    return

memo = {}
def ways(G, current, target):
    if current == target:
        return 1
    if (current, target) in memo:
        return memo[(current, target)]
    else:
        if current in G: 
            tot = 0
            for v in G[current]:
                tot += ways(G,v, target)
            memo[(current,target)] = tot
            return tot
    return 0
            
with open(filename) as f:
    data = {x.split(" ")[0][:-1]:x.split(" ")[1:] for x in f.read().splitlines()}
    #explore(data, "svr", "svr")
    #import graphviz
    #g = graphviz.Graph('G', filename='test.gv')
    #for k,v in data.items():
    #    for dest in v:
    #        g.edge(k,dest)
    #g.view()
    p1 = ways(data, "svr", "fft")
    p2 = ways(data, "fft", "dac")
    p3 = ways(data, "dac", "out")
    print(p1*p2*p3)
