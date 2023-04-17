n, m, k = map(int, input().split())
grid = [list(map(lambda x: ord(x)-ord('A'), input())) for y in range(n)]
a = [i for i in range(k)]
for x in range(m):
    for y in range(1, n):
        if a[grid[y][x]] != a[grid[y-1][x]]:
            a[grid[y][x]] = a[grid[y-1][x]]
print(len(set(a)))