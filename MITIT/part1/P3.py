MOD = 10**9+7

for _ in range(int(input())):
    H,W = map(int, input().split())
    grid = [input() for _ in range(H)]

    def inBounds(x,y):
        return x >= 0 and x < W and y >= 0 and y < H

    processed = set()
    def solve():
        ways = 1
        for y in range(H):
            for x in range(W):
                if grid[y][x] == "o" and (x,y):
                    options = 0
                    for dx1,dy1,dx2,dy2 in [(0,1,1,0),(0,1,-1,0),(0,-1,-1,0),(0,-1,1,0)]:
                        x1,y1,x2,y2 = x+dx1,y+dy1,x+dx2,y+dy2
                        if inBounds(x1,y1) and inBounds(x2,y2) and grid[y1][x1] == "." and grid[y2][x2] == ".":
                            options += 1
                    if options == 0:
                        return 0
                    else:
                        ways = (ways*options) % MOD

        return ways
    
    print(solve())