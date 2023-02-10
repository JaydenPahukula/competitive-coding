N, M = map(int, input().split())

#build maze
maze = [[' ' for _ in range(M)] for _ in range(N)]
dots = []
for y in range(N):
    row = input()
    for x, c in enumerate(row):
        maze[y][x] = c
        if c == '.':
            dots.append((y, x))

players = 0
unreachable = 0
while len(dots) > 0:
    startingy, startingx = dots[0]

    #BFS
    foundplayer = False
    q = [(startingy, startingx)]
    discovered = [(startingy, startingx)]
    visiteddots = 0
    while len(q) > 0:
        #pop from the queue
        (y, x), *q = q
        c = maze[y][x]

        #check if on a dot
        if c == '.' and (y, x) in dots:
            dots.remove((y, x))
            visiteddots += 1

        #check all adjacent spots
        for y1, x1 in [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]:
            if (y1, x1) not in discovered and maze[y1][x1] in " .":
                q.append((y1, x1))
                discovered.append((y1, x1))
            elif not foundplayer and maze[y1][x1] not in " .X":
                foundplayer = True

    if foundplayer:
        players += 1
    else:
        unreachable += visiteddots

print(players, unreachable)