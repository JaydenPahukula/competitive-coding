
# for _ in range(int(input())):
#     h, w = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(h)]
#     p = [[(y, x) for x in range(w)] for y in range(h)]

#     def union(a:tuple, b:tuple):
#         p[a[0]][a[1]][0] = find(b)

#     def find(a:tuple):
#         if p[a[0]][a[1]][0] == a[0] and p[a[0]][a[1]][1] == a[1]:
#             return a
#         result = find(p[a[0]][a[1]])
#         p[a[0]][a[1]] = result
#         return result
    
#     for y in range(h):
#         for x in range(w):
#             if 
    




from collections import deque

for _ in range(int(input())):
    h, w = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    maxVolume = 0
    for starty in range(h):
        for startx in range(w):
            if visited[starty][startx]: continue
            if not grid[starty][startx]: continue

            q = deque()
            q.append((startx, starty))
            volume = 0
            while q:
                x, y = q.pop()
                if visited[y][x]: continue
                visited[y][x] = True
                volume += grid[y][x]
                if y > 0 and not visited[y-1][x] and grid[y-1][x]: q.append((x, y-1))
                if x > 0 and not visited[y][x-1] and grid[y][x-1]: q.append((x-1, y))
                if y < h-1 and not visited[y+1][x] and grid[y+1][x]: q.append((x, y+1))
                if x < w-1 and not visited[y][x+1] and grid[y][x+1]: q.append((x+1, y))
            
            if volume > maxVolume:
                maxVolume = volume
    
    print(maxVolume)
