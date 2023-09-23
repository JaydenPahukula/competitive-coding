
def check(grid):
    players = {1:"X",2:"O"}
    for p in range(1,3):
        for x in range(3):
            if grid[x][0] == p and grid[x][1] == p and grid[x][2] == p:
                return f"{players[p]} wins"
            if grid[0][x] == p and grid[1][x] == p and grid[2][x] == p:
                return f"{players[p]} wins"
        if grid[0][0] == p and grid[1][1] == p and grid[2][2] == p:
            return f"{players[p]} wins"
        if grid[2][0] == p and grid[1][1] == p and grid[0][2] == p:
            return f"{players[p]} wins"
    for y in range(3):
        for x in range(3):
            if grid[y][x] == 0:
                return "In progress"
    return "Cat's"

for _ in range(int(input())):
    s = [c=="1" for c in bin(int(input(),8))[2:]]
    s = list(reversed([False for _ in range(19-len(s))]+s))
    grid = [[0,0,0] for _ in "123"]
    for i in range(9):
        if s[i]:
            if s[i+9]: grid[i//3][i%3] = 1
            else: grid[i//3][i%3] = 2
    print(check(grid))