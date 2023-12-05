n = int(input())

def numIslands(l:list):
    cutoff = min(l)
    l1 = []
    total = 0
    for i in range(len(l)):
        if l[i] > cutoff:
            l1.append(l[i])
        elif l1:
            total += 1 + numIslands(l1)
            l1 = []
    if l1:
        total += 1 + numIslands(l1)
    return total
    

for i in range(n):
    print(i+1, numIslands(list(map(int, input().split()))[1:]))