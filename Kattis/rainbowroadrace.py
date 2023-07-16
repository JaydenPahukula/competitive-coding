import heapq

rb = {"R":0, "O":1, "Y":2, "G":3, "B":4, "I":5, "V":6}
n, m = map(int, input().split())
connections = [[] for _ in range(n)]
for _ in range(m):
    i, j, d, color = input().split()
    connections[int(j)-1].append((int(i)-1, int(d), rb[color]))
    connections[int(i)-1].append((int(j)-1, int(d), rb[color]))

visited = set()
q = [(0, 0, 0)]
while q:
    total, icolors, curr = heapq.heappop(q)
    colors = -icolors

    if colors == 127 and curr == 0:
        print(total)
        break

    if (128*curr)+colors in visited: continue
    visited.add((128*curr)+colors)

    for neighbor, d, color in connections[curr]:
        if (128*neighbor)+(colors | 2**color) not in visited:
            heapq.heappush(q, (total+d, -(colors | 2**color), neighbor))