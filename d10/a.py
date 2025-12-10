import sys
sys.setrecursionlimit(1000000)
filename = sys.argv[1]
visited = {} # state -> times
ans = []
def press_button(B,s) -> str:
    n = ""
    for i,c in enumerate(s):
        if i in B:
            if c == "#": n += "."
            else: n += "#"
        else:
            n += c
    return n


def explore(cs, p, buttons, ts):
    #print(cs, p, buttons)
    if cs == ts:
        ans.append(p)
        return
    for B in buttons:
        #simulate press
        n = press_button(B, cs)
        if (n not in visited) or (n in visited and visited[n] > p+1):
            visited[n] = p+1
            explore(n, p+1, buttons, ts)        

        
with open(filename) as f:
    data = f.read().splitlines()
    configs = [x.split(" ")[0] for x in data]
    buttons = [x.split(" ")[1:-1] for x in data]
    t = 0
    for B,C in zip(buttons, configs):
        B = [tuple(map(int,x[1:-1].split(","))) for x in B]
        C = C[1:-1]
        explore("."*len(C), 0, B, C)
        print(min(ans))
        t += min(ans)
        ans.clear()
        visited.clear()
    print(t)


