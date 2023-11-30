import heapq

n, k, m = map(int, input().split())
T, w = map(int, input().split())
snatchers = set(map(int, input().split()))

roads = [[] for _ in range(n)]
for _ in range(m):
    a,b,d = map(int, input().split())
    a,b = a-1,b-1
    roads[a].append((b,d))
    roads[b].append((a,d))

# get distance to end
distToEnd = [-1 for _ in range(n)]
q = [(0, n-1)]
visited = [False for _ in range(n)]
while q:
    totalDist, curr = heapq.heappop(q)

    if visited[curr]: continue
    visited[curr] = True
    distToEnd[curr] = totalDist

    for neighbor, dist in roads[curr]:
        if not visited[neighbor]:
            heapq.heappush(q, (totalDist+dist, neighbor))

print(distToEnd)



