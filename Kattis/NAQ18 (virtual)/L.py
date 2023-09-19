n, k = map(int, input().split())
grid = [[-1 for _ in range(n)] for _ in range(n)]
gridrows = [set() for _ in range(n)]
gridcols = [set() for _ in range(n)]
for y in range(k):
    for x, num in enumerate(map(int, input().split())):
        grid[y][x] = num
        gridrows[y].add(num)
        gridcols[x].add(num)


for y in range(k):
    if len(gridrows[y]) != n:
        print("no")
        exit()
for x in range(n):
    if len(gridcols[x]) != k:
        print("no")
        exit()

print("yes")
for y in range(k, n):
    for x in range(n):
        for num in range(1, n+1):
            if num not in gridrows[y] and num not in gridcols[x]:
                grid[y][x] = num
                gridrows[y].add(num)
                gridcols[x].add(num)
                break
        else:
            print("something broke")
print(grid)