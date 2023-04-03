n, m = map(int, input().split())
pa, pb = map(int, input().split())
connections = [[] for _ in range(n)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    connections[p1].append(p2)
    connections[p2].append(p1)

q = [pa]
discovered = set()
t = 0
while 1:
    qlen = len(q)
    for i in range(qlen):
        currPlanet = q[i]

        if currPlanet == pb:
            break

        for p in connections[currPlanet]:
            if p not in discovered:
                q.append(p)
                discovered.add(p)
    else:
        t += 1
        q = q[qlen:]
        continue
    break

print((t+1)//2)
