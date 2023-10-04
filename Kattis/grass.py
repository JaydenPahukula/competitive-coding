import sys
lines = sys.stdin.readlines()
linei = 0

def covers(x:float, r:float, W:float):
    d = (r**2-(W/2)**2)**(0.5)
    return x-d, x+d

while linei < len(lines):

    n, L, W = map(int, lines[linei].split())
    sprinklers = [tuple(map(int, lines[1+linei+i].split())) for i in range(n)]
    cover = sorted([covers(*sprinklers[i], W) for i in range(n)])

    curr, numUsed = 0, 0
    for i in range(n):
        if curr >= L: break
        if cover[i][0] > curr: break
        if i < n-1 and cover[i+1][0] <= curr: continue
        numUsed += 1
        curr = cover[i][1]

    if curr < L: print(-1)
    else: print(numUsed)

    linei += 1+n
