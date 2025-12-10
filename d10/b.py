import sys
import time
from copy import deepcopy
from z3 import * 
sys.setrecursionlimit(1000000)
filename = sys.argv[1]
visited = {} # state -> times
ans = []
memo = {}
def press_button(B,s) -> str:
    n = list(s)
    for index in B:
        n[index] += 1
    return tuple(n)

def unpress_button(B,s) -> str:
    n = list(s)
    for index in B:
        n[index] -= 1
    return tuple(n)

def valid(cs,ts,buttons):
    lefts = [x-y for x,y in zip(ts,cs)]
    print(cs,ts,lefts)
    for index in range(len(cs)):
        lfi = lefts[index] # missing presses for that position
        if lfi == 0: continue
        valids = 0 # look for valid buttons
        cbutt = [b for b in buttons if index in b]
        for button in cbutt:
            # all left values for keys must be >= lfi for button to be valid
            if all([lefts[k] >= lfi for k in button]):
               break
        else:
            return False
        return True


def solve(B, ts):
    s = Optimize()
    vars = [Int(f'x{i}') for i in range(len(B))]
    for i, res in enumerate(ts):
        terms = []
        for j, b in enumerate(B):
            if i in b:
                terms.append(vars[j])
        if terms:
            s.add(Sum(terms) == res)
        else:
            s.add(0 == res)
    for v in vars:
        s.add(v >= 0)
    s.minimize(Sum(vars))
    if s.check() == sat:
        model = s.model()
        for v in vars:
            print(f"{v} =", model[v])
        total = sum(model[v].as_long() for v in vars)
        return total
    else:
        print("Impossible")

def explore(cs, p, buttons, ts):
    #print(cs,p,ts)
    if cs == ts:
        ans.append(p)
        return
    #if not valid(cs,ts,buttons): return
    for B in buttons:
        #simulate press
        n = press_button(B, cs)
        if (n not in visited) or (n in visited and visited[n] > p+1):
            if all([x<=y for x,y in zip(n, ts)]):
                visited[n] = p+1
                explore(n, p+1, buttons, ts)


def dp(cs, ts,buttons):
    # cs is always 0 0 0 ... 0
    # returns min presses to get from cs to ts
    if ts in memo: return memo[ts]
    if cs == ts: return 0
    if any([y<x for x,y in zip(cs,ts)]):
        return float("inf")
    poss = []
    for B in buttons:
        nts = unpress_button(B,ts)
        poss.append(dp(cs, nts, buttons))
    ans = min(poss)+1
    memo[ts] = ans
    return ans
    

with open(filename) as f:
    data = f.read().splitlines()
    #configs = [x.split(" ")[0] for x in data]
    buttons = [x.split(" ")[1:-1] for x in data]
    joltage = [x.split(" ")[-1] for x in data]
    t = 0
    for B,J in zip(buttons, joltage):
        B = [tuple(map(int,x[1:-1].split(","))) for x in B]
        J = list(map(int,J[1:-1].split(",")))
        res = solve(B, J)
        t += res
        #print(B,J)
        #explore(tuple([0]*len(J)), 0, B, tuple(J))
        #print(min(ans))
        #t+=min(ans)
        #ans = dp(tuple([0]*len(J)), tuple(J), B)
        #print(ans)
        #t += ans
        #ans.clear()
        #visited.clear()
        #memo.clear()
    print(t)


