import heapq

n, m = map(int, input().split())
conn = [{} for _ in range(n)]
for _ in range(m):
    a, b, l = map(int, input().split())
    if b in conn[a]:
        conn[a][b] = min(conn[a][b], l)
    else:
        conn[a][b] = l
    if a in conn[b]:
        conn[b][a] = min(conn[b][a], l)
    else:
        conn[b][a] = l

visited = set()
q = [(0, 0)]
maxLen = 0
while q:
    l, curr = heapq.heappop(q)

    maxLen = max(maxLen, l)
    visited.add(curr)
    if len(visited) == n: break

    for neighbor in conn[curr].keys():
        if neighbor in visited: continue
        heapq.heappush(q, (conn[curr][neighbor], neighbor))

if len(visited) == n:
    print(maxLen)
else:
    print("IMPOSSIBLE")
