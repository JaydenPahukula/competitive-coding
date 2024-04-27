import sys
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split()))+[-1] for _ in range(n)]

    for x in range(n):
        s = set()
        thing = -1
        for y in range(n):
            thingy = grid[y][x]
            if thingy in set:
                thing = thingy
                break
        for y in range(n):
            if grid[y][x] != thingy:
                for x1 in range(n-1,x-1,-1):
                    

print("\n".join(map(str, out)))
