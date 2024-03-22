import sys
from collections import deque
input=sys.stdin.readline

out = []
for _ in range(int(input())):
    n,k = map(int, input().split())
    adj = [None]+[[] for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    leaf = 1
    while len(adj[leaf]) > 1: leaf += 1
    count = 0
    q = deque([(leaf,k,-1)])
    while q:
        curr,currk,parent = q.popleft()

        if currk == 1: count += 1
        if currk == 0: currk = k+1

        for neighor in adj[curr]:
            if neighor == parent: continue
            q.append((neighor,currk-1,curr))
    out.append(count)
print("\n".join(map(str, out)))
