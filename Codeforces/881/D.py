import sys
sys.setrecursionlimit(500000)

for _ in range(int(input())):
    n = int(input())
    connections = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        connections[u-1].append(v-1)
        connections[v-1].append(u-1)
    
    tree = [[] for _ in range(n)]
    q = [(0, -1)]
    leaves = set()
    while q:
        curr, parent = q.pop()
        if len(connections) == 1 and curr != 0:
            leaves.add(curr)
        for child in connections[curr]:
            if child == parent: continue
            tree[curr].append(child)
            q.append((child, curr))

    l = [0 for _ in range(n)]


    def numLeafDescendants(num:int):
        if l[num] != 0:
            return l[num]
        else:
            if len(tree[num]) == 0:
                l[num] = 1
                return 1
            else:
                total = 0
                for child in tree[num]:
                    total += numLeafDescendants(child)
                l[num] = total
                return total

    numQueries = int(input())
    for _ in range(numQueries):
        a, b = map(int, input().split())
        print(numLeafDescendants(a-1) * numLeafDescendants(b-1))