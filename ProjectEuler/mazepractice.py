MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0 ,0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
start = (1, 1)
end = (5, 19)

def printMaze(maze):
    print()
    for row in maze:
        s = ""
        for num in row:
            if num == 0:
                s += '  '
            elif num == 1:
                s += '##'
            elif num == 2:
                s += '::'
            elif num == 3:
                s += "[]"
        print(s)

def solution(maze):

    q = [start]
    discovered = set()
    tb = {}
    while len(q) != 0:
        (y,x), *q = q
        maze[y][x] = 2

        if (y, x) == end:
            break

        if (y, x) in discovered:
            continue
        else:
            discovered.add((y,x))


        if maze[y+1][x] == 0:
            q.append((y+1, x))
            tb[(y+1,x)] = (y,x)
        if maze[y-1][x] == 0:
            q.append((y-1, x))
            tb[(y-1,x)] = (y,x)
        if maze[y][x+1] == 0:
            q.append((y, x+1))
            tb[(y,x+1)] = (y,x)
        if maze[y][x-1] == 0:
            q.append((y, x-1))
            tb[(y,x-1)] = (y,x)

        discovered.add((y,x))

    curr = end
    path = []
    while curr != start:
        maze[curr[0]][curr[1]] = 3
        path.append(curr)
        curr = tb[curr]
    maze[curr[0]][curr[1]] = 3
    path.append(curr)

    printMaze(maze)
    return path[::-1]

print(solution(MAZE))