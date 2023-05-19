import heapq

n, m, x, y = map(int, input().split())
x -= 1
y -= 1
villages = [[] for _ in range(n)]
for _ in range(m):
    a, b, w, c = map(int, input().split())
    a -= 1
    b -= 1
    villages[a].append((int(c == 2), int(c == 1), w, b))
    villages[b].append((int(c == 2), int(c == 1), w, a))

visited = [False for _ in range(n)]
q = [(0, 0, 0, x)]
while q:
    currTitans, currShamans, currLength, currVillage = heapq.heappop(q)

    if currVillage == y:
        print(currLength, currShamans, currTitans)
        break

    if visited[currVillage]: continue
    visited[currVillage] = True

    for titans, shamans, length, destination in villages[currVillage]:
        if visited[destination]: continue
        heapq.heappush(q, (currTitans+titans, currShamans+shamans, currLength+length, destination))
else:
    print("IMPOSSIBLE")

