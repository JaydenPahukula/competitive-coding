import heapq

n, m = map(int, input().split())
lodging = list(map(int, input().split()))
roads = [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    roads[u-1].append((v-1, a, b))
    roads[v-1].append((u-1, a, b))

alfurCost = {}
q = [(0,0)]
while q and len(alfurCost) < n:
    cost, curr = heapq.heappop(q)
    if curr in alfurCost: continue
    else: alfurCost[curr] = cost
    for destination, a, b in roads[curr]:
        if destination in alfurCost: continue
        heapq.heappush(q, (cost+a, destination))

benediktCost = {}
q = [(0,n-1)]
while q and len(benediktCost) < n:
    cost, curr = heapq.heappop(q)
    if curr in benediktCost: continue
    else: benediktCost[curr] = cost
    for destination, a, b in roads[curr]:
        if destination in benediktCost: continue
        heapq.heappush(q, (cost+b, destination))

print(min([alfurCost[i]+benediktCost[i]+lodging[i] for i in range(n)]))