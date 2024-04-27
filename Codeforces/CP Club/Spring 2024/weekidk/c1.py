
def idk():
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    a = grid[0][0]
    b = grid[1][0]
    if a == b: return False
    for y in range(n):
        for x in range(n):
            if x == y or x == n-1-y:
                if grid[y][x] != a: return False
            else:
                if grid[y][x] != b: return False
    return True

if idk():
    print("YES")
else:
    print("NO")
