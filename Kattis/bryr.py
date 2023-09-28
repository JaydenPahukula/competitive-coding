import heapq

n, m = map(int, input().split())
roads = [[] for _ in range(n)]
for _ in range(m):
    a, b, bridge = map(int, input().split())
    roads[a-1].append((bridge, b-1))
    roads[b-1].append((bridge, a-1))

q = [(0,0)]
seen = set()
while q:
    numSingle, curr = heapq.heappop(q)

    for isSingle, destination in roads[curr]:
        if destination == n-1: print(numSingle+isSingle); exit()
        if destination in seen: continue
        heapq.heappush(q, (numSingle+isSingle, destination))
        seen.add(destination)
else:
    while 1: n += 1