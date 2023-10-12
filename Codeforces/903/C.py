for _ in range(int(input())):
    n = int(input())
    grid = [[c for c in input()] for _ in range(n)]
    count = 0
    
    for y in range(n//2):
        for x in range(n//2):
            vals = [ord(x) for x in [grid[y][x], grid[x][n-1-y], grid[n-1-y][n-1-x], grid[n-1-x][y]]]
            mx = max(vals)
            count += sum([mx-x for x in vals])
    
    print(count)