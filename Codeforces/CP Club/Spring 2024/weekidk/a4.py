import sys
input=sys.stdin.readline

def run():
    h,w = map(int,input().split())
    grid = [list(input()) for _ in range(h)]
    out = [["." for _ in range(w)] for _ in range(h)]
    hdoms = [[] for _ in range(w-1)]
    vdoms = [[] for _ in range(h-1)]

    for y in range(h-1):
        for x in range(w):
            if grid[y][x] == "U":
                vdoms[y].append(x)
    
    for x in range(w-1):
        for y in range(h):
            if grid[y][x] == "L":
                hdoms[x].append(y)

    for y in range(h-1):
        if len(vdoms[y])%2:
            print(-1)
            return
        for i in range(0,len(vdoms[y]),2):
            x1 = vdoms[y][i]
            x2 = vdoms[y][i+1]
            out[y][x1] = "B"
            out[y+1][x1] = "W"
            out[y][x2] = "W"
            out[y+1][x2] = "B"
    
    for x in range(w-1):
        if len(hdoms[x])%2:
            print(-1)
            return
        for i in range(0,len(hdoms[x]),2):
            y1 = hdoms[x][i]
            y2 = hdoms[x][i+1]
            out[y1][x] = "B"
            out[y1][x+1] = "W"
            out[y2][x] = "W"
            out[y2][x+1] = "B"
    
    for y in range(h):
        print("".join(out[y]))
        

for _ in range(int(input())):
    run()
