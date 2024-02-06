from collections import deque

for _ in range(int(input())):
    n,m = map(int, input().split())
    adj = [None]+[[] for _ in range(n)]
    minEdges = []
    minWeight = 10**6+1
    for _ in range(m):
        a,b,w = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        if w < minWeight:
            minWeight = w
            minEdges = [(a,b)]
        elif w == minWeight:
            minEdges.append((a,b))

q = deque()
for x in q:
    print(x)