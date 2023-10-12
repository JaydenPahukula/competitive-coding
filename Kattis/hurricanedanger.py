from math import hypot

def distanceToLine(line:tuple, x:int, y:int):
    x1,y1,x2,y2 = line
    if x1==x2: return abs(x-x1)
    if y1==y2: return abs(y-y1)
    def xt(t): return t*(x2-x1)+x1
    def yt(t): return t*(y2-y1)+y1
    
    lo = -10**6
    hi = 10**6
    best = 10**6
    while hi-lo > 0.00000001:
        m1 = lo+(hi-lo)/3
        m2 = lo+2*(hi-lo)/3
        dist1 = hypot(x-xt(m1), y-yt(m1))
        dist2 = hypot(x-xt(m2), y-yt(m2))
        if dist1 < dist2: hi = m2
        else: lo = m1
        best = min(best, dist1, dist2)
    return best

for _ in range(int(input())):
    line = tuple(map(int, input().split()))
    m = int(input())
    best = 10**6
    out = []
    for _ in range(m):
        name, x, y = input().split()
        d = distanceToLine(line, int(x), int(y))
        if abs(d-best) < 0.000001:
            out.append(name)
        elif d < best:
            best = d
            out = [name]
    print(" ".join(out))