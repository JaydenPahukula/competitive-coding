import heapq

n,m = map(int, input().split())
adj = [None]+[[] for _ in range(n)]
for _ in range(m):
    a,b,c,r = map(int, input().split())
    adj[a].append((b,c,r))
    adj[b].append((a,c,r))

visited = set()
q = [(0,0,1,False)]
while q:
    lowestNeg, coins, curr, infinite = heapq.heappop(q)
    coins = -coins

    if curr == n or infinite:
        print(lowestNeg)
        break

    if curr in visited: continue
    visited.add(curr)

    for neighbor,c,r in adj[curr]:
        heapq.heappush(q, (max(lowestNeg, -coins+c), -coins+c-r, neighbor, r>c))
