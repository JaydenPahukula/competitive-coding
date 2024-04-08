import sys
from math import gcd
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    h,w = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]

    mem = {}
    def dp(x,y):
        if (x,y) == (0,0): return grid[0][0]
        if (x,y) in mem: return mem[(x,y)]
        result = -1
        if x > 0:
            result = gcd(grid[y][x], dp(x-1,y))
        if y > 0:
            result = max(result, gcd(grid[y][x], dp(x,y-1)))
        mem[(x,y)] = result
        return result
    out.append(dp(w-1,h-1))
    print(mem)

print("\n".join(map(str, out)))
