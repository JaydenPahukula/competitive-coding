parent = []

def union(a:int, b:int):
    heada = find(a)
    headb = find(b)
    if heada != headb:
        parent[heada] = headb
    return

def find(num:int):
    if parent[num] == num:
        return num
    head = find(parent[num])
    parent[num] = head
    return head

n, e, p = map(int, input().split())
treehouses = []
connected = set()
for i in range(n):
    if i < e:
        parent.append(0)
    else:
        parent.append(i)
    x, y = map(float, input().split())
    treehouses.append((x, y, i))
for _ in range(p):
    a, b = map(int, input().split())
    union(a-1, b-1)

possibleBridges = []
for x, y, i in treehouses[:-1]:
    for x1, y1, j in treehouses[i+1:]:
        if find(i) != find(j):
            possibleBridges.append((((x1-x)**2+(y1-y)**2)**(1/2), i, j))
possibleBridges.sort()

total = 0
for distance, a, b in possibleBridges:
    if find(a) != find(b):
        union(a, b)
        total += distance

print(total)