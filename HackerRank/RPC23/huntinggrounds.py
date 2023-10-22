n, q = map(int, input().split())
grid = [[0 for _ in range(n+1)]]+[[0]+list(map(int, input().split())) for _ in range(n)]

# 2d prefix sum
for y in range(n+1):
    for x in range(1,n+1):
        grid[y][x] += grid[y][x-1]
for x in range(n+1):
    for y in range(1,n+1):
        grid[y][x] += grid[y-1][x]

# answer queries
for _ in range(q):
    y1,x1,y2,x2 = map(int, input().split())
    print(grid[y2][x2] - grid[y2][x1-1] - grid[y1-1][x2] + grid[y1-1][x1-1])