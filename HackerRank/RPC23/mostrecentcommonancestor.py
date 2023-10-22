n = int(input())
a = {}

for _ in range(n):
    ancestor, descendant = input().split(" -- ")
    a[descendant] = ancestor

def lineage(dino):
    if dino not in a: return []
    ancestor = a[dino]
    return [ancestor]+lineage(ancestor)

la = lineage(input())
lb = lineage(input())
for a in la:
    for b in lb:
        if a == b:
            print(a)
            exit()
