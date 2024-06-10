from collections import deque

n = int(input())
grid = [input() for _ in range(n)]
dist = [[-1 for _ in range(n)] for _ in range(n)]

q = deque()
spies = []
for y in range(n):
    for x in range(n):
        if grid[y][x] == "H":
            q.append((x,y,0))
        elif grid[y][x] == "S":
            spies.append((x,y))

while q:
    x,y,d = q.popleft()
    if y < 0 or y >= n or x < 0 or x >= n: continue
    if dist[y][x] != -1: continue
    dist[y][x] = d
    for dy,dx in [(0,1),(1,0),(0,-1),(-1,0)]:
        q.append((x+dx,y+dy,d+1))

out = 0
for x,y in spies:
    out = max(out, dist[y][x])
print(out)
