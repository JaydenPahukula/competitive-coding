import heapq

n, m = map(int, input().split())
grid = [input().split() for _ in range(n)]
start = (0,0)
for y in range(n):
    for x in range(m):
        if grid[y][x] == "D": start = (x,y)

if n == 0 or m == 0: 
    print(-1)
    exit()

q = [(0, 0, start)]
visited = [[False for _ in range(m)] for _ in range(n)]
out = []
while q:
    distance, canyonsJumped, (x, y) = heapq.heappop(q)

    if visited[y][x]: continue
    visited[y][x] = True

    if grid[y][x] == "P" and (x == 0 or x == m-1 or y == 0 or y == n-1):
        out.append(distance)
        continue

    for x1, y1 in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n: continue
        if grid[y1][x1] == "P": heapq.heappush(q, (distance+1, canyonsJumped, (x1,y1)))
        if grid[y1][x1] == "C" and canyonsJumped < 5: heapq.heappush(q, (distance+1, canyonsJumped+1, (x1,y1)))

if out: print(min(out))
else: print(-1)
