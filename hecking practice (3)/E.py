from collections import deque

n = int(input())
l = [0 for _ in range(n)]
bonds = [() for _ in range(n-1)]
conns = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    bonds[i] = (int(a)-1, int(b)-1)
    conns[int(a)-1].append(int(b)-1)
    conns[int(b)-1].append(int(a)-1)

visited = set()
outie = [True for _ in range(n)]
q = deque([(0, 0)])
while q:
    curr, dist = q.pop()

    visited.add(curr)
    outie[curr] = bool(dist % 2)

    for neighbor in conns[curr]:
        if neighbor in visited: continue
        q.appendleft((neighbor, dist+1))

for a, b in bonds:
    print(int(outie[a]))