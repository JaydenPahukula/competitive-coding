import heapq

N, M = map(int, input().split())
sizes = {}
connections = {}
for i in range(N):
    connections[i+1] = []
bridges = []
for _ in range(M):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)
for i in range(N):
    sizes[i+1] = int(input())

q = []
for x in connections[1]:
    heapq.heappush(q, (sizes[x], x))
conquered = {1}
armySize = sizes[1]
while 1 and len(q) > 0:
    size, island = heapq.heappop(q)

    if island in conquered: continue
    if size >= armySize: break

    conquered.add(island)
    armySize += sizes[island]

    for possibleIsland in connections[island]:
        heapq.heappush(q, (sizes[possibleIsland], possibleIsland))

print(armySize)