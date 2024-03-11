import heapq

for _ in range(int(input())):
    n,m = map(int,input().split())
    idk = [[] for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        idk[a-1].append((b-1,c))
        idk[b-1].append((a-1,c))
    start,end = map(int,input().split())
    q = [(0,start-1,-1)]
    visited = set()
    while q:
        x,curr,color = heapq.heappop(q)

        if curr == end-1:
            print(x)
            break

        if (curr,color) in visited: continue
        visited.add((curr,color))

        for neighbor,c in idk[curr]:
            if c == color:
                heapq.heappush(q,(x,neighbor,c))
            else:
                heapq.heappush(q,(x+1,neighbor,c))
