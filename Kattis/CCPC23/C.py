h, w, n = map(int, input().split())
grid = [list(input()) for _ in range(h)]


for i in range(h):
    print(" ".join(grid[i]))

constellations = []
for y in range(h):
    for x in range(w):
        if grid[y][x] == "*":
            constellations