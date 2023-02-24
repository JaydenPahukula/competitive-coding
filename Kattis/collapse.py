N = int(input())
demand = [0 for _ in range(N)]
supply = [0 for _ in range(N)]
receives = [[] for _ in range(N)]
feeds = [[] for _ in range(N)]
for i in range(N):
    inp = list(map(int, input().split()))
    demand[i] = inp[0]
    for j in range(2, len(inp), 2):
        receives[i].append((inp[j]-1, inp[j+1]))
        supply[i] += inp[j+1]
        feeds[inp[j]-1].append((i, inp[j+1]))

collapsed = {0}
q = [0]
while q:
    curr = q.pop()

    for island, amt in feeds[curr]:
        if island in collapsed: continue
        supply[island] -= amt
        if supply[island] < demand[island]:
            collapsed.add(island)
            q.append(island)

print(N-len(collapsed))